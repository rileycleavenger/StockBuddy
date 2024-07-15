# Use the official Python image from the Docker Hub
FROM python:3.11

# Define Chrome version
ENV CHROME_VERSION=123.0.6312.122-1

# Add Google Chrome repository
COPY chromeInstall.sh /usr/local/bin/chromeInstall.sh
RUN chmod +x /usr/local/bin/chromeInstall.sh

# Run the chromeInstall.sh script
RUN /usr/local/bin/chromeInstall.sh

# Set display port to avoid crash
ENV DISPLAY=:99

# Set the working directory in the container to /scraper
WORKDIR /scraper

# Copy the current directory contents into the container at /scraper
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to the outside world
EXPOSE 8080

# Run scraper.py when the container launches
CMD ["python3", "scraper.py"]
