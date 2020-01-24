from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time,json,os
from pprint import pprint
import time

browser=webdriver.Chrome("/home/naguruul/Desktop/chromedriver")
browser.get("https://www.zomato.com/ncr")

from selenium.webdriver.common.keys import Keys
response = browser.execute_script('return document.documentElement.outerHTML')
# browser.quit()
soup =  BeautifulSoup(response,"html.parser")
div = soup.find("div",class_="ui segment row")


def zomato_hotle():
	place=div.find_all("a")
	dic={}
	list1=[]
	for i in place:
		link=i["href"]
		list1.append(link)
	url=list1[0]
	browser=webdriver.Chrome("/home/naguruul/Desktop/chromedriver")
	browser.get(url)
	response=browser.execute_script('return document.documentElement.outerHTML')
	browser.quit()
	soup = BeautifulSoup(response,"html.parser")
	detail=soup.find("div",id="orig-search-list",class_="ui cards")
	name=detail.find_all("div",class_="card search-snippet-card search-card")
	for j in name:
		n=j.find("a",class_="result-title hover_feedback zred bold ln24 fontsize0").get_text()
		l=''
		for k in n.split():
				l+=k+' '
		dic["name"]=l
		rating=j.find("div",class_="ta-right floating search_result_rating col-s-4 clearfix").get_text().split()
		dic["rating"]=rating[0]
		dic[rating[-1]]=rating[1]
		schedule=j.find("div",class_="search-page-text clearfix row")
		food=schedule.find("div",class_="clearfix")
		if food!=None:
			food=food.find('span',class_="col-s-11 col-m-12 nowrap pl0").text
			dic["food"]=food[1:]
		price=schedule.find("div",class_="res-cost clearfix")
		if price!=None:
			price=price.find('span',class_="col-s-11 col-m-12 pl0").text
			dic["price"]=price
		hour=schedule.find("div",class_="res-timing clearfix")
		if hour!=None:
			hour=hour.find('div',class_="col-s-11 col-m-12 pl0 search-grid-right-text").text
			dic["hour"]=hour.strip()
		feature=schedule.find("div",class_="res-collections clearfix")
		if feature!=None:	
			dic["feature"]=feature.text[13:].strip()
		pprint(dic)
			
		

				

zomato_hotle()




