import requests
import urllib
import Queue
import threading
import re
import sys
import json

class MovieInformation():
	def __init__(self, title, year, director):
		self.title = title
		self.year = year
		self.director = director

class Imdb():
	server = 'http://www.omdbapi.com/?'
	queue = Queue.Queue()

	def __init__(self, title):
		self.title = title

	def recoverInformation(self):
		self.title = re.sub(r'(.*\/)*', "",self.title)
		self.title = re.sub(r'\..*', "",self.title)
		url = self.server + 't=' + self.title + '&y=&plot=short&r=json'
		#print url
		try:
			request = requests.get(url)
			if request.status_code == 200:
				answer = json.loads((request.text))
				#print answer['Response']
				if answer['Response'] == "True":
					self.queue.put(answer)
					return

				#if answer["Response"] == "True":
					#return answer

				else:
					self.queue.put("Not found")
					return
			else:
				self.queue.put("Result failed")
				return
		except :
			print sys.exc_info()[0]
			self.queue.put("Server failed")
			return

	def main(self):
		t = threading.Thread(target = self.recoverInformation)
		t.start()
		t.join()
		data = self.queue.get()
		#print data
		if data != "Server failed" and data != "Result failed" and data != "Not found":
			movie = MovieInformation(data['Title'], data['Year'], data['Director'])
			return movie
		else:
			return None
