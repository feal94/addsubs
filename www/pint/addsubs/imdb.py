import requests
import urllib

class Movie():
	def __init__(self, title, year, director):
		self.title = title
		self.year = year
		self.director = director

class Imdb():
	server = 'http://www.omdbapi.com/?'

	def __init__(self, title):
		self.title = title

	def recoverInformation(self):
		#method = 'GET'
		#timeout = 500
		url = self.server + 't=' + self.title + '&y=&plot=short&r=json'
		try:
			request = requests.get(url)
			if request.status_code == 200:
				answer = (request.text)
				if answer["Response"] == "True": 
					return answer
				else:
					return "Not found"
			else:
				return "Result failed"
		except:
			return "Server failed"

	def main(self):
		data = self.recoverInformation()
		if data != "Server failed" and data != "Result failed" and data != "Not found": 
			movie = Movie(data["Title"], data["Year"], director["Director"])
			return movie
		else:
			return "Fallo en IMBD"
