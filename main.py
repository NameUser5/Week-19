from bs4 import BeautifulSoup
import requests

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

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


# Scrape the population of each country into a list -- DONE

print(color.GREEN + color.BOLD + "\nScrape the population of each country into a list -- DONE" + color.END)
population_list = []
populations = soup.find_all('span',{'class':'country-population'})
for _ in populations:
    population_list.append(_.text)

for _ in population_list:
    print(_)

# Scrape and print the title of the page -- DONE
print(color.GREEN + color.BOLD + "\nScrape and print the title of the page -- DONE" + color.END)
title = soup.title.text
print(title)

# # What NOT to do--> Note: this prints the entire span, including the tags
# pop = soup.select(".country-population")
# print(pop)


# Scrape and print the second hyperlink on the site. -- DONE (?)

print(color.YELLOW + color.BOLD + "\nScrape and print the second hyperlink on the site. -- DONE (?)" + color.END)
hyperlink_list = []
hyperlinks = soup.find_all('a')
for _ in hyperlinks:
    hyperlink_list.append(_)

# Taking the entire tag instead of just the text , so I can see what is being linked.
print(hyperlink_list[1])


# # How many h3 tags are on the site -- DONE
print(color.GREEN + color.BOLD + "\nHow many h3 tags are on the site -- DONE \n" + color.END)
heading_three_list = []
headings = soup.find_all('h3')
count = 0
for _ in headings:
    heading_three_list.append(_)
    count += 1

print(f"There are {count} h3 headings on this page.\n")


# Scrape and print the area of all countries that start with the letter 's' -- IN PROGRESS

print(color.RED + color.BOLD + "\nScrape and print the area of all countries that start with the letter 's' -- IN PROGRESS" + color.END)
countries = soup.find_all('div', {'class':'col-md-4 country'})

for country in countries:
    country_name = (country.h3.text.strip())
    # if country_name.startswith("S"):
    #     area = country.find('class'='country-area').text
    #     print(f"{country_name}, Area: {area}")
    if country_name.startswith("D"):
        capital = country.find(class_="country-capital").text
        print(f"{country_name}, Capital: {capital}")


# Scrape and print the capitals that start with the letter 'd'

print(color.RED + color.BOLD + "\nScrape and print the capitals that start with the letter 'd' -- DONE" + color.END)
#
# for country in countries:
#     country_name = (country.h3.text.strip())
#     if country_name.startswith("D"):
#         capital = country.find(class_="country-capital").text
#         print(f"{country_name}, Capital: {capital}")

# h_tags = soup.find_all('h3',{'class':'country-name'})
# capitals = soup.find_all('span',{'class':'country-capital'})
# populations = soup.find_all('span',{'class':'country-population'})
# areas = soup.find_all('span',{'class':'country-capital'})
#
# population_list = []
# populations = soup.find_all('span',{'class':'country-population'})
# for _ in populations:
#     population_list.append(_.text)
#
# capital_list = []
# capitals = soup.find_all('span',{'class':'country-capital'})
# for _ in capitals:
#     capital_list.append(_.text)
#
# area_list = []
# areas = soup.find_all('span',{'class':'country-capital'})
# for _ in areas:
#     area_list.append(_.text)
#
# count = 0
# country_names = []
# h_tags = soup.find_all('h3',{'class':'country-name'})
# for _ in h_tags:
#     country_names.append(_.text)
#     count += 1
#
# class Country_info():
#     def __init__(self,country_names):
#
#         for _ in country_names:
#             idx = country_names.index(_)
#
#         self.country_capital = capitals.index(idx)
#         self.country_population = populations.index(idx)
#         self.country_area = areas.index(idx)
#
# for _ in h_tags:
#     if _.text[0] == 'S':
#         idx = h_tags.index(_)
#         print(_.text,capitals.index(idx),populations.index(idx),areas.index(idx))

# for _ in h_tags:
#     country_names.append(_.text)
#
# for _ in country_names:
#     if _[0] == 'S' or 's':
#         idx = country_names.index(_)
#         print(_,capitals.index(idx),populations.index(idx),areas.index(idx))


# for _ in country_names:
#     if _[0].upper() == letter:
#         print(_)
#
#
# area_list = soup.find_all('span',{'class':'country-area'})



# Scrape and print data for Panama only.
# count = 0
# for _ in h_tags:
#     country_names.append(_)
#     count += 1
# for _ in country_names:
#     if _ == 'Panama':
#         idx = country_names.index(_)
#         print(country_names.index(idx),capital_list.index("Panama"),population_list.index(count),area_list.index(count))
# #
# print(capitals.index(1))