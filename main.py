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

# # Scrape and print the title of the page -- DONE
# title = soup.title.text
# print(title)


# # Scrape the population of each country into a list -- DONE
#
# population_list = []
# populations = soup.find_all('span',{'class':'country-population'})
# for _ in populations:
#     population_list.append(_.text)
#
# for _ in population_list:
#     print(_)

# # What NOT to do--> Note: this prints the entire span, including the tags
# pop = soup.select(".country-population")
# print(pop)


# # Scrape and print the second hyperlink on the site. -- DONE (?)
#
# hyperlink_list = []
# hyperlinks = soup.find_all('a')
# for _ in hyperlinks:
#     hyperlink_list.append(_)
#
# # Taking the entire tag instead of just the text , so I can see what is being linked.
# print(hyperlink_list[1])


# # How many h3 tags are on the site -- DONE
#
# heading_three_list = []
# headings = soup.find_all('h3')
# count = 0
# for _ in headings:
#     heading_three_list.append(_)
#     count += 1
#
# print(f"There are {count} h3 headings on this page.")


# Scrape and print the area of all countries that start with the letter 's' -- IN PROGRESS

letter = 'S'

h_tags = soup.find_all('h3',{'class':'country-name'})
capitals = soup.find_all('span',{'class':'country-capital'})
populations = soup.find_all('span',{'class':'country-population'})
areas = soup.find_all('span',{'class':'country-capital'})

country_names = []

for _ in h_tags:
    country_names.append(_.text)

class Country_info():
    def __init__(self,country_names):

        for _ in country_names:
            idx = country_names.index(_)

        self.country_capital = capitals.index(idx)
        self.country_population = populations.index(idx)
        self.country_area = areas.index(idx)

for _ in country_names:
    if _[0] == 'S':
        idx = country_names.index(_)
        print(_.text,capitals.index(idx),populations.index(idx),areas.index(idx))
# for _ in country_names:
#     if _[0].upper() == letter:
#         print(_)
#
#
# area_list = soup.find_all('span',{'class':'country-area'})



# Scrape and print data for Panama only.

# for _ in country_h_tags:
#     if _.text == 'Panama':
#         data = soup.select("country-capital")