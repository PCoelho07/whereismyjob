#-*- encoding: utf-8 -*- 

from ProgramathorScraper import ProgramathorScraper
import os

if __name__ == '__main__':
	sc = ProgramathorScraper()
	print "Starting the " + type(sc).__name__ + " crawller"
	sc.get_jobs_list()
	sc.to_csv('dados_programathor.csv')
	print "Done!"




