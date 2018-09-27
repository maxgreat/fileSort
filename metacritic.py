import urllib.request
import urllib.parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import googlesearch3
from googlesearch import search


def findCritic(title):
	s_query = ' '.join([title, 'metacritic'])
	lst = search(s_query, stop = 1)
	top_1 = list(lst)[0]
	req = Request(top_1, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()

	html = str(webpage)
	soup = BeautifulSoup(html, 'html.parser')
	try:
		critics = soup.find('span', {'itemprop':'ratingValue'})
		critics = critics.text
	except Exception as e:
		critics = 'NaN'
	try:
		users = soup.find('div', {'class':'user'})
		users = users.text
	except Exception as e:
		users = 'NaN'
	
	try:
		genre = soup.find('li', {'class':'product_genre'})
		genre = genre.text.replace('Genre(s):', '')
		genre = genre.replace(' ', '')
		genre = genre.replace(',', ', ')
	except Exception as e:
		genre = 'NaN'
	return title, critics, users, genre


def criticGames(fileName='Games.csv', test=False):
	with open('Games.csv', 'r') as file:
		lines = file.readlines()
		lines = lines[1:]

		if test:
			print(findCritic(lines[0].split(',')[0]))
			return
		
		for line in lines:	
			title = line.split(',')[0]
			print(findCritic(title))



if __name__=='__main__':
	criticGames(test=True)
