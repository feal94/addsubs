import requests
import urllib
import Queue
import threading

class Movie():
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
		#method = 'GET'
		#timeout = 500
		print "Entrar entra, A ver"
		url = self.server + 't=' + self.title + '&y=&plot=short&r=json'
		try:
			request = requests.get(url)
			if request.status_code == 200:
				answer = (request.text)
				if answer["Response"] == "True": 
					self.queue.put(answer)
					return
				else:
					self.queue.put("Not found")
					return 
			else:
				self.queue.put("Result failed")
				return 
		except:
			self.queue.put("Server failed")
			return 

	def main(self):
		t = threading.Thread(target = self.recoverInformation)
		t.start()
		t.join()
		data = self.queue.get()
		#data = self.recoverInformation()
		if data != "Server failed" and data != "Result failed" and data != "Not found": 
			movie = Movie(data["Title"], data["Year"], director["Director"])
			return movie
		else:
			return "Fallo en IMBD"
