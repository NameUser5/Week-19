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

print(color.GREEN + color.BOLD + "\nScrape the population of each country into a list." + color.END)
population_list = []
populations = soup.find_all('span',{'class':'country-population'})
for _ in populations:
    population_list.append(_.text)

for _ in population_list:
    print(_)

# Scrape and print the title of the page -- DONE
print(color.GREEN + color.BOLD + "\nScrape and print the title of the page." + color.END)
title = soup.title.text
print(title)

# # What NOT to do--> Note: this prints the entire span, including the tags
# pop = soup.select(".country-population")
# print(pop)


# Scrape and print the second hyperlink on the site. -- DONE

print(color.GREEN + color.BOLD + "\nScrape and print the second hyperlink on the site." + color.END)
hyperlink_list = []
hyperlinks = soup.find_all('a')
for _ in hyperlinks:
    hyperlink_list.append(_)

# Taking the entire tag instead of just the text , so I can see what is being linked.
print(hyperlink_list[1])


# # How many h3 tags are on the site -- DONE
print(color.GREEN + color.BOLD + "\nHow many h3 tags are on the site?" + color.END)
heading_three_list = []
headings = soup.find_all('h3')
count = 0
for _ in headings:
    heading_three_list.append(_)
    count += 1

print(f"There are {count} h3 headings on this page.")


# Scrape and print the area of all countries that start with the letter 's' -- DONE
print(color.GREEN + color.BOLD + "\nScrape and print the area of all countries that start with the letter 's'." + color.END)

all_countries = soup.find_all('div', class_="col-md-4 country")

for _ in all_countries:
    country_name = (_.h3.text.strip())
    if country_name.startswith("S"):
        area = _.find(class_="country-area").text
        print(f"{country_name}, {area} sq. km")


# Scrape and print data for Panama only. -- DONE
print(color.GREEN + color.BOLD + "\nScrape and print data for Panama only." + color.END)

countries = soup.find_all('div', class_="col-md-4 country")

for _ in countries:
    country = (_.h3.text.strip())
    if country == ("Panama"):
        capital = _.find(class_="country-capital").text
        population = _.find(class_="country-population").text
        area = _.find(class_="country-area").text
        print(f" {country}-- Capital: {capital}, Pop.: {population}, Area: {area} sq. km")

for _ in all_countries:
    country_name = (_.h3.text.strip())
    country_info = _.find(class_="country-info")
    info_text = (_.text.strip())
    if country == ("Panama"):
        print(info_text)


# Scrape and print the capitals that start with the letter 'd' -- DONE
print(color.GREEN + color.BOLD + "\nScrape and print the capitals that start with the letter 'd'." + color.END)

all_capitals = soup.find_all('span', class_="country-capital")

for capitals in all_capitals:
    capital_name = (capitals.text.strip())
    if capital_name.startswith("D"):
        print(f"{capital_name}")

print(color.YELLOW + color.BOLD + "\nMethod 2" + color.END)

countries = soup.find_all('div', class_="col-md-4 country")

for _ in all_countries:
    country_name = (_.h3.text.strip())
    country_info = _.find(class_="country-info")
    country_capital = (_.text.strip())
    if country_capital.startswith("D"):
        capital = country_info.find(class_="country-capital").text
        print(f"{country_capital}, {country_name}")