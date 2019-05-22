import bs4 as bs
import requests

WIKI_URL = 'https://pt.wikipedia.org/wiki/Lista_de_companhias_citadas_no_Ibovespa'

def get_ibovespa_tickers(url):
	resp = requests.get(url).text
	soup = bs.BeautifulSoup(resp, 'lxml')
	table = soup.find('table', {'class': 'wikitable sortable'})

	tickers = []
	for row in table.findAll('tr')[1:]:
		ticker = row.findAll('td')[0].text
		ticker = ticker[:4]
		tickers.append(ticker)

	return tickers
