import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


#driver = webdriver.Chrome()
#driver.get("https://www.nami.org/Personal-Stories/")
URL= "https://www.mentalhealthforum.net/forum/mental-health-issues-and-experiences/mental-health-experiences/index2.html"
notes =[]
def thredbit_new():
	page1 = soup.find_all("li",{"class":"threadbit new"})
	for article in page1:
		for info in soup.find_all("div",{"class":"threadinfo"}):
			for title in soup.find_all("a",{"class":"title"}):
				sentences = title.text.replace("\n"," ").strip()
				print(sentences)
				notes.append(sentences)

def threadbit():
	page2 = soup.find_all("li",{"class":"threadbit"})
	for article in page2:
		for info in soup.find_all("div",{"class":"threadinfo"}):
			for title in soup.find_all("a",{"class":"title"}):
				sentences = title.text.replace("\n"," ").strip()
				print(sentences)
				notes.append(sentences)	

def threadbit_hot():
	page2 = soup.find_all("form",{"id":"thread_inlinemod_form"})
	for article in page2:
		for title in soup.find_all("a",{"class":"title"}):
			sentences = title.text.replace("\n"," ").strip()
			print(sentences)
			notes.append(sentences)					


for i in range(3,400):
	url = requests.get(URL)
	data = url.text
	soup = BeautifulSoup(data,'html.parser')
	#threadbit()
	threadbit_hot()
	#thredbit_new()
	print(i)
	URL = "https://www.mentalhealthforum.net/forum/mental-health-issues-and-experiences/mental-health-experiences/" + "index" + str(i) + ".html"
	print(URL)
"""		
"""		
"""
	url_tag = soup.find("a",{"class":"unselectedNext"})
	if url_tag.get("href"):
		URL = "https://www.nami.org/Personal-Stories/?page=1" + url_tag.get('href')
	else:
		break	
"""

Notes = list(set(notes))
dataFrame = pd.DataFrame(Notes)
dataFrame.to_csv("med_data.csv", mode='a', header=False)
