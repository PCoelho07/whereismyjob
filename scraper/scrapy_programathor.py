# -*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


LINK_PAGE = 'https://programathor.com.br/jobs?remoto=true'

def get_page_content(): 
	response = requests.get(LINK_PAGE)
	page_content = BeautifulSoup(response, "html.parser")
	return page_content

def get_jobs_list():
	page_content = get_page_content()
	wrapper_jobs = page_content.find(class_="wrapper-jobs-list")
	jobs = wrapper_jobs.find(class_="container").find_all(class_="cell-list")

	job_links = []
	job_names = []

	for job in jobs:
		job_names.append(job.find("a").get("href"))
		job_links.append(job.find(class_="cell-list-content").h3.string)


def save():
	


if __name__ == '__main__':
	get_jobs_list()
