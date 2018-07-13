# -*- encoding: utf-8 -*- 

import requests as re
import pandas as pd
import os
from bs4 import BeautifulSoup

class Scraper(object):
	
	__url = ''
	result = {}

	def __init__(self, url):
		self.__url = url

	def set_url(self, url):
		self.__url = url

	def get_url(self):
		return self.__url

	def get_content_page(self):
		response = re.get(self.__url)
		page_content = BeautifulSoup(response.content, "html.parser")

		return page_content

	def get_jobs_list(self):
		pass

	def to_csv(self, file_name):
		path = os.path.join(os.path.dirname(__file__), 'data')
		dataframe = pd.DataFrame.from_dict(self.result)
		dataframe.to_csv(os.path.join(path, file_name), encoding='utf-8')




