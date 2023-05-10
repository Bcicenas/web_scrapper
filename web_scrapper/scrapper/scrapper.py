# Scrapper class
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

class Scrapper:
	def __init__(self, name, url):
		self.name = name
		self.url = url
		req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read()		
		self.soup = BeautifulSoup(webpage, "html.parser")

	def find_all(self, search_text):
		return self.soup.find_all(search_text) if search_text else self.soup.prettify()

