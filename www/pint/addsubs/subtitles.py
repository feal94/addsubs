import requests
import urllib
import os
import hashlib
from imdb import Movie
from imdb import Imdb
#import eventlet
import Queue
import threading

class MovieInformation():
	#server = 'http://api.thesubdb.com/?action='
	server = 'http://sandbox.thesubdb.com/?action='
	queue = Queue.Queue()
	
	def __init__(self, name, lang):
		self.language= lang
		self.name = name
		self.user_agent= {
			'User-Agent': 'SubDB/1.0 (AddSubs/1.0;https://github.com/feal94/addsubs)'
		}
		self.hash= self.get_hash()
		
		
	def get_hash(self):
		readsize = 64 * 1024
		with open(self.name, 'rb') as f:
			size = os.path.getsize(self.name)
			data = f.read(readsize)
			f.seek(-readsize, os.SEEK_END)
			data += f.read(readsize)
		return hashlib.md5(data).hexdigest()

	def check(self):
		#This list all available languages for a movie
		#method = 'GET'
		timeout = 500
		action = 'search'
		hash = 'hash=' + self.hash
		url = self.server + action + '&' + hash
		try:
			request = requests.get(url, headers=self.user_agent)
			if request.status_code == 200:
				self.queue.put(request.text)
				return 
			else:
				self.queue.put("Result failed")
				return 
		except:
			self.queue.put("Server failed")
			return 


	def download(self):
		#method = 'GET'
		timeout = 500
		action = 'download'
		hash = 'hash=' + self.hash
		language = 'language=' + self.language
		url = self.server + action + '&' + hash + '&' + language
		try:
			request = requests.get(url, headers=self.user_agent)
			if request.status_code == 200:
				self.queue.put(request.text)
				return  
			elif request.status_code == 404:
				self.queue.put("Not avaliable")
				return  
			elif request.status_code == 400:
				self.queue.put("Malformed request")
				return  
		except:
			self.queue.put("Server failed")
			return  


	def main(self):
		t = threading.Thread(target = self.check)
		t.start()
		t.join()
		answer = self.queue.get()
		if answer != "Result failed" and answer != "Server failed":
			if self.language in answer:
				t = threading.Thread(target = self.download)
				t.start()
				t.join()
				subtitles = self.queue.get()
				if subtitles != "Malformed request":
					imdb = Imdb(self.name)  #aqui falta elmiminar antes la ruta
					information = imdb.main()
				#agregar informacion a subtitulos
					return subtitles
			else:
				return answer

