from selenium import webdriver  # Need To import webdriver from selenium package
from bs4 import BeautifulSoup as bs
import re
global positive

driver = webdriver.Chrome("/Users/shivika/Albany-SUNY/MastersProject/chromedriver")
driver.get("https://www.famousbirthdays.com/march12.html")
html = driver.page_source
driver.close()

soup = bs(html, "xml")

celeb_name = []
celeb_detail = []
celeb_rank = []

name = soup.find_all('div', class_='name')
for info in name:
	celeb_name.append(info.text.strip())

detail = soup.find_all('div', class_="title hidden-xs")
for details in detail:
	celeb_detail.append(details.text.strip())

rn = soup.find_all('span', class_='rank')
for rnk in rn:
	celeb_rank.append(rnk.text.strip())


# print "Sentiment Analysis for Birthday Celebrities:"
# print '--------------------------------------------------------------------------------------------'
# print "Name of Celebrity, Profession and Rank : "
#
# for i in range(0,40):
# 	print ' Celebrities Name:  ' + (celeb_name[i]), '\n', ' Profession : ' + (celeb_detail[i]), '\n', ' Celebrity Rank:' + (celeb_rank[i]), '\n'
