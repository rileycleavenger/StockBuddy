from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

gainers_url = 'https://stockanalysis.com/markets/gainers/'
losers_url = 'https://stockanalysis.com/markets/losers/'
news_url = 'https://stockanalysis.com/news/'

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

def extractHeadlines(url):
    driver.get(url)
    headlines = driver.find_elements(by="xpath", value='//div[contains(@class, "wrsb")]//div[contains(@class, "uncontain")]//div[contains(@class, "mb-2 flex flex-col space-y-3 overflow-x-hidden bg-gray-200 dark:bg-dark-950 sm:space-y-0 sm:bg-white dark:sm:bg-dark-800 lg:border-0")]//div[contains(@class, "gap-4 border-gray-300 bg-white p-4 shadow last:pb-1 last:shadow-none dark:border-dark-600 dark:bg-dark-800 sm:border-b sm:px-0 sm:shadow-none sm:last:border-b-0 lg:gap-5 sm:grid sm:grid-cols-news sm:py-6")]')

    headline_data = []
    for headline in headlines:
        title = headline.find_element(by = "xpath", value = './/div[contains(@class, "lex flex-col")]//h3[contains(@class, "mb-2 mt-3 text-xl font-bold leading-snug sm:order-2 sm:mt-0 sm:leading-tight")]//a[contains(@class, "text-default hover:text-blue-brand_sharp dark:text-neutral-300 dark:hover:text-blue-darklink")]').text
        link = headline.find_element(by = "xpath", value = './/div[contains(@class, "lex flex-col")]//h3[contains(@class, "mb-2 mt-3 text-xl font-bold leading-snug sm:order-2 sm:mt-0 sm:leading-tight")]//a[contains(@class, "text-default hover:text-blue-brand_sharp dark:text-neutral-300 dark:hover:text-blue-darklink")]').get_attribute('href')
        headline_data.append((title, link))
    return headline_data

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

print("\nHeadlines\n")

headlines = extractHeadlines(news_url)

for title, link in headlines:
    print(title)
    print(link)
    print("")

driver.quit()  # Close the driver when done
