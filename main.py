# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv

def save_csv(smarts):
	with open('info.csv','w', encoding = 'utf-8') as f:
		writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
		writer.writerow(("Товар","Цена","Ссылка"))
		for info in smarts:
			writer.writerow((info['title'],info['price'],info['link']))


def parse():
	URL = 'https://bt.rozetka.com.ua/refrigerators/c80125/'
	headers = {
		"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
	   }

	response = requests.get(URL, headers=headers)
	soup = BeautifulSoup(response.content, "lxml")
	items = soup.findAll("div", class_ = 'goods-tile__inner')
	smarts = []

	for item in items:
		smarts.append({
			'title': item.find('a', class_ = 'goods-tile__heading ng-star-inserted').text.strip(),
			'price': item.find('p', class_ = 'ng-star-inserted').text.strip(),
			'link': item.find('a', class_ = 'goods-tile__heading ng-star-inserted').get('href')
			})

		for smart in smarts:
			print(smart['title'],"Цена > ",smart['price'],smart['link'])
			save_csv(smarts)

parse()


		