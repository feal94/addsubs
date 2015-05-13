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
		url = self.server + 't=' + title + '&y=&plot=short&r=json'
		try:
			request = requests.get(url)
			if request.status_code == 200:
				answer = (request.text)
				return answer
			else:
				return "Result failed"
		except:
			return "Server failed"

	def main(self):
		data = self.recoverInformation()
		movie = Movie(data["Title"], data["Year"], director["Director"])
		return movie
