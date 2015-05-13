import requests
import urllib


class MovieInformation():
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

	def saveInformation(self, data):
		title = data["Title"]
		year = data["Year"]
		director = data["Director"]
		movie=Movie(title=title,director=director,year=year)
		movie.save()


	def main(self):
		data = self.recoverInformation()
		self.saveInformation(data)
