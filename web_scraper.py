import time as t
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import io
import pandas as pd
from selenium.common.exceptions import NoSuchElementException


path = "D:\\New Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)

body = driver.find_element_by_tag_name('body')


List = []
 
url = "https://www.time-to-change.org.uk/category/blog/school%2C-college-and-university"


for i in range(1,139):
	driver.get(url)
	driver.implicitly_wait(10)
	html = driver.page_source
	data = soup(html)
	page = data.find_all("section",{"class":"nodes"})
	for article in page:
		for summary in data.find_all("div",{"class":"node-content"}):
			sentences = summary.text.replace("\n"," ").strip()
			print(sentences)
			List.append(sentences)
			print(i)
			url = "https://www.time-to-change.org.uk/category/blog/school%2C-college-and-university" + "?page=" + str(i)
			print(url)


  
List = list(set(List))
dataFrame = pd.DataFrame(List)
dataFrame.to_csv("med_data.csv", mode='a', header=False)

driver.close()