# -*- encoding: utf-8 -*-

from Scraper import Scraper

class ProgramathorScraper(Scraper):
	"""docstring for ClassName"""
	def __init__(self):
		super(ProgramathorScraper, self).__init__("https://programathor.com.br/jobs?remoto=true")
		

	def get_jobs_list(self):
		url_context = 'https://programathor.com.br'
		wrapper_jobs = self.get_content_page().find(class_="wrapper-jobs-list")
		jobs = wrapper_jobs.find(class_="container").find_all(class_="cell-list")
		job_links = []
		job_names = []

		for job in jobs:
			job_names.append(job.find("a").get("href"))
			job_links.append( url_context + job.find(class_="cell-list-content").h3.string)


		self.result = {
			'name': job_names,
			'url': job_links
		}



