import requests
import urllib
import eventlet

class MovieInformation():
	#server = 'http://api.thesubdb.com/?action='
	server = 'http://sandbox.thesubdb.com/?action='

	def __init__(self, name):
		self.name = name
		self.user_agent= {
			'User-Agent': 'SubDB/1.0 (AddSubs/1.0;https://github.com/feal94/addsubs)'
		}
	def get_hash(self):
		readsize = 64 * 1024
		with open(name, 'rb') as f:
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
			with eventlet.Timeout(timeout)
				request = requests.get(url, headers=self.user_agent)
			if request.status_code == 200:
				return request.text
			else:
				return "Result failed"
		except:
			return "Server failed"


	def download(self):
		#method = 'GET'
		timeout = 500
		action = 'download'
		hash = 'hash=' + self.hash
		language = 'language=' + self.language
		url = self.server + action + '&' + hash + '&' + language
		try:
			with eventlet.Timeout(timeout)
				request = requests.get(url, headers=self.user_agent)
			if request.status_code == 200:
				return request.text
			elif request.status_code == 404
				return "Not avaliable"
			elif request.status_code == 400
				return "Malformed request"
		except:
			return "Server failed"


	def main(self):
		return 'hello'
		#self.hash = self.get_hash()
		#answer = self.check()
		#if answer != "Result failed" and answer != "Server failed":
		#	subtitles = self.download()
		#	return subtitles
		#else:
		#	return answer
