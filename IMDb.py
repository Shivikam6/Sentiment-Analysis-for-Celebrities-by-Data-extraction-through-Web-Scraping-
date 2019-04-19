from selenium import webdriver  # Need To import webdriver from selenium package
from bs4 import BeautifulSoup as bs
import string
from string import digits
from time import sleep
global positive

driver = webdriver.Chrome("/Users/shivika/Albany-SUNY/MastersProject/chromedriver")
driver.get("https://www.imdb.com/search/name?birth_monthday=03-12")
html = driver.page_source
driver.close()

soup = bs(html, "xml")

celeb_name = []
celeb_rank=[]
celeb_detail=[]
for eachName in soup.find_all('div', class_="lister-item-content"):
	eachH3 = eachName.findChildren('h3', class_="lister-item-header")[0]
	celeb_name.append(eachH3.find('a').text.strip())
	celeb_rank.append(eachH3.find('span', class_='lister-item-index unbold text-primary').text.strip())
	eachPara = eachName.findChildren('p', class_="text-muted text-small")[0]
	for trash1 in eachPara(['span','a']):
		trash1.decompose()
	celeb_detail.append(eachPara.text.strip())

# print "Sentiment Analysis for Birthday Celebrities:"
# print '--------------------------------------------------------------------------------------------'
# print "Name of Celebrity , Profession and Rank: "
#
# for i in range(0,40):
# 	print ' Celebrities Name:  ' + (celeb_name[i]), '\n', ' Profession : ' + (celeb_detail[i]), '\n', ' Celebrity Rank:' + (celeb_rank[i]), '\n'

# def Final_Output():