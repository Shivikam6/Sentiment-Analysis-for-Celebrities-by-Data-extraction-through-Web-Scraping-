from selenium import webdriver          # Import webdriver from selenium package
from bs4 import BeautifulSoup as bs     # Import Web Scraping library
import string
from string import digits
from time import sleep
from csv import writer
import csv

global positive
import re

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.imdb.com/search/name?birth_monthday=03-12")
html = driver.page_source
driver.close()

soup = bs(html, "xml")                  # Parsing the html page

# searching for the classes and storing the content in variables
eachNames = soup.find_all('div', class_="lister-item-content")

## Saving the data in one CSV file called imdb.csv
with open("imdb.csv", "w") as file:
	writer = csv.writer(file)
	writer.writerow(['Name', 'Profession', 'Rank'])
	
	for eachName in eachNames:
		eachH3 = eachName.findChildren('h3', class_="lister-item-header")[0]
		cname = eachH3.find('a').text.encode('utf-8').strip()
		crank = eachH3.find('span', class_='lister-item-index unbold text-primary').text.strip()
		eachPara = eachName.findChildren('p', class_="text-muted text-small")[0]
		profession = eachPara.text.strip()
		matchObj = re.search("(\w+)", profession)
		if matchObj:
			profession = matchObj.group(1)
		writer.writerow([cname, profession, crank])