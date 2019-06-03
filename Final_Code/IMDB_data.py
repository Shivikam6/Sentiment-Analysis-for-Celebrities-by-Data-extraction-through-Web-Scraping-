from selenium import webdriver          # Import webdriver from selenium package
from bs4 import BeautifulSoup as bs     # Import Web Scraping library
import string
from string import digits
from time import sleep
global positive
import re                               # Import regex

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.imdb.com/search/name?birth_monthday=03-12")
html = driver.page_source
driver.close()

soup = bs(html, "xml")                  # Parsing the html page

celeb_name = []
celeb_rank = []
celeb_detail = []

# searching for the classes and storing the content in variables
for eachName in soup.find_all('div', class_="lister-item-content"):
	
	eachH3 = eachName.findChildren('h3', class_="lister-item-header")[0]
	celeb_name.append(eachH3.find('a').text.strip())
	
	celeb_rank.append(eachH3.find('span', class_='lister-item-index unbold text-primary').text.strip())
	
	eachPara = eachName.findChildren('p', class_="text-muted text-small")[0]
	profession = eachPara.text.strip()
	matchObj = re.search("(\w+)", profession)
	if matchObj:
		profession = matchObj.group(1)
	celeb_detail.append(profession)


# for i in range(0,len(celeb_name)):
# 	print 'celeb name: '+celeb_name[i]