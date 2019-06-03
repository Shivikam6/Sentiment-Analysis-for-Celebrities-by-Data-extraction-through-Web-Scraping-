from selenium import webdriver          # Import webdriver from selenium package
from bs4 import BeautifulSoup as bs     # Import Web Scraping library
import re
from csv import writer
import csv
global positive

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.famousbirthdays.com/march12.html")
html = driver.page_source
driver.close()

soup = bs(html, "xml")                  # Parsing the html page

# searching for the classes and storing the content in variables
celebs = soup.find_all('a', class_='face person-item')

## Saving the data in one CSV file called FamousBirthdays.csv
with open('FamousBirthdays.csv', 'w') as file:
	writer = writer(file)
	writer.writerow(['Name', 'Profession', 'Rank'])
	
	for celeb in celebs:
		cname = celeb.find('div', class_='name').text.strip()
		matchObj = re.search("(\w+\s\w+|\w+),", cname)
		if matchObj:
			cname = matchObj.group(1)
		
		prof = celeb.find('div', class_="title hidden-xs").text.strip()
		crank = celeb.find('span', class_='rank').text.strip()
		
		writer.writerow([cname, prof, crank])
		