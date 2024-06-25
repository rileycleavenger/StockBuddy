from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

gainers_url = 'https://stockanalysis.com/markets/gainers/'
losers_url = 'https://stockanalysis.com/markets/losers/'

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Function to scrape a URL for stock information
def extractCompanies(url):
    driver.get(url)
    companies = driver.find_elements(by = "xpath", value = '//table//tbody//tr[contains(@class, "svelte-eurwtr")]')
    
    company_data = []
    for company in companies:
        name = company.find_element(by = "xpath", value = './/td[contains(@class, "slw svelte-eurwtr")]').text
        symbol = company.find_element(by = "xpath", value = './/td[contains(@class, "sym svelte-eurwtr")]').text
        if url == 'https://stockanalysis.com/markets/gainers/': # When the URL is for gainers
            percent = company.find_element(by = "xpath", value = './/td[contains(@class, "rg svelte-eurwtr")]').text
        else:
            percent = company.find_element(by = "xpath", value = './/td[contains(@class, "rr svelte-eurwtr")]').text
        price = company.find_element(by = "xpath", value = './/td[contains(@class, "svelte-eurwtr")][5]').text
        company_data.append((name, symbol, percent, price))
    return company_data

# Printing in terminal for testing purposes
# Extract gainers
print("\nGainers\n")

gainers = extractCompanies(gainers_url)

for name, symbol, percent, price in gainers:
    print(name)
    print(symbol)
    print(percent)
    print("$" + price)
    print("")

# Extract losers
print("\nLosers\n")

losers = extractCompanies(losers_url)

for name, symbol, percent, price in losers:
    print(name)
    print(symbol)
    print(percent)
    print("$" + price)
    print("")

driver.quit()  # Close the driver when done
