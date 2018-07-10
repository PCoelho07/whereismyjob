# -*- encoding: utf-8 -*- 

import requests as re
import pandas as pd
from bs4 import BeautifulSoup

class Scraper(object):
	
	__url = ''
	__result = {}

	def __init__(self, url):
		self.__url = url

	def set_url(self, url):
		self.__url = url

	def get_url(self):
		return self.__url

	def get_content_page(self):
		response = re.get(self.__url)
		page_content = BeautifulSoup(response.content, "html.parse")

		return page_content

	def get_jobs_list():
		pass

	def to_csv(self, file_name):
		dataframe = pd.DataFrame.from_dict(self.__result, oriented="index")
		dataframe.to_csv(file_name)




