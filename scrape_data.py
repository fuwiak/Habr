#-*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


URL = 'http://txtmusic.ru/index.php?s=%D0%F3%EA%E8+%C2%E2%E5%F0%F5%21'

page = urllib.request.urlopen(URL)
soup = BeautifulSoup(page)

li = soup.body.findAll('li') # <li>

names_of_songs= [str(x)[str(x).index('<b>Руки Вверх!')+len('<b>Руки Вверх! - '):str(x).index('</b>')] for x in li]


URLS = ['http://txtmusic.ru/'+l.a.get('href') for l in li]


df = pd.DataFrame(columns=['name', 'text'])

list_of_names = []
list_of_text = []

ind=0
BIG = ""
for URL in URLS:
	page = urllib.request.urlopen(URL)
	soup = BeautifulSoup(page)
	article = soup.body.findAll('article')
	text = str(article[0]).split('\n')[8]
	text = text.split('<br/>')
	text = [t for t in text if t!='']
	text = " ".join(text)

	name= str(article[0].h1).split(" - ")[1].rstrip("</h1>")
	list_of_text.append(text)
	list_of_names.append(name)


df.name = list_of_names
df.text = list_of_text

#df.to_csv('songs.csv')
