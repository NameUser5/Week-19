from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = BeautifulSoup(page.content, 'html.parser')

# Scrape the population of each country into a list
# Scrape and print the title of the page.
# Scrape and print the second hyperlink on the site.
# How many h3 tags are on the site.
# Scrape and print the area of all countries that start with the letter 's'
# Scrape and print data for Panama only.
# Scrape and print the capitals that start with the letter 'd'

# Scrape and print the title of the page -- DONE
title = soup.title.text
print(title)

# Scrape the population of each country into a list
populations = []

# for _ in range(251):
#     country_pop = soup.select(".country-population")
#     populations += country_pop
#     print(populations)

# country_pop = soup.select("country-population")
# print(country_pop)