from bs4 import BeautifulSoup
import requests

url = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(url)
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

# Note: this prints the entire span, including the tags
pop = soup.select(".country-population")
print(pop)

# Scrape the population of each country into a list -- DONE

population_list = []
population = soup.find_all('span',{'class':'country-population'})
for _ in population:
    population_list.append(_.text)

for _ in population_list:
    print(_)