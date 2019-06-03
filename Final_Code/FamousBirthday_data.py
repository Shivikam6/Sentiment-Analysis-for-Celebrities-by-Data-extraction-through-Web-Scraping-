from selenium import webdriver          # Import webdriver from selenium package
from bs4 import BeautifulSoup as bs     # Import Web Scraping library
import re                               # Import regex
from csv import writer
import csv

global positive

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.famousbirthdays.com/march12.html")
html = driver.page_source
driver.close()

soup = bs(html, "xml")                  # Parsing the html page

celeb_name = []
celeb_detail = []
celeb_rank = []

# searching for the classes and storing the content in variables
celebs = soup.find_all('a', class_='face person-item')

for celeb in celebs:
	cname = celeb.find('div', class_='name').text.strip()
	matchObj = re.search("(\w+\s\w+|\w+),", cname)
	if matchObj:
		cname = matchObj.group(1)
	celeb_name.append(cname)
	
	celeb_detail.append(celeb.find('div', class_="title hidden-xs").text.strip())
	celeb_rank.append(celeb.find('span', class_='rank').text.strip())

# for i in range(0,len(celeb_name)):
#  	print 'celeb name: '+celeb_name[i]