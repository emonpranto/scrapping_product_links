# Web Scraping Daraz Bangladesh Routers Products
### Description
This Python script scrapes product URLs from the routers category on Daraz Bangladesh using Selenium. The script navigates through all available pages, extracts product links from each page, and stores them in a dictionary for later use. The script calculates the number of pages based on the total product count and extracts the URLs of products listed on each page.

### Features
- Scrapes product links from all pages of the routers category.
- Handles pagination and calculates the total number of pages.
- Collects product links across multiple pages (up to 40 products per page).
- Handles exceptions gracefully, ensuring that errors during scraping don't halt the script.

### Requirements
To run this script, you will need:

- Python 3.x
- Selenium library
- Chrome WebDriver installed and available in the system's PATH.

For additional support for run this code i have uploaded the requirements.txt file where you can find all the libraries you need. 
