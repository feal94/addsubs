import requests
import urllib


class MovieInformation():
	#server = 'http://api.thesubdb.com/?action='
	server = 'http://sandbox.thesubdb.com/?action='

	def __init__(self, name, languages):
		self.name = name
		self.language= languages

	def get_hash(self):
		readsize = 64 * 1024
		with open(name, 'rb') as f:
			size = os.path.getsize(self.name)
			data = f.read(readsize)
			f.seek(-readsize, os.SEEK_END)
			data += f.read(readsize)
		return hashlib.md5(data).hexdigest()

	def check(self):
		method = 'GET'
		timeout = 500
		action = 'search'
		hash = 'hash=' + self.hash
		url = self.server + action + '&' + hash
		try:
			request = requests.request(method, url, timeout)
			if request.status_code == 200:
				return request.text
			#answer = eval(request.text)
			#if answer["result"] == "success":
			#	return answer["data"]
			else:
				return "Result failed"
		except:
			return "Server failed"


	def download(self):
		method = 'GET'
		timeout = 500
		action = 'download'
		hash = 'hash=' + self.hash
		language = 'language=' + self.language
		url = self.server + action + '&' + hash + '&' + language
		try:
			request = requests.request(method, url, timeout)
			if request.status_code == 200:
				return request.text
			#answer = eval(request.text)
			#if answer["result"] == "success":
				#return answer["data"]
			else:
				return "Result failed"
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
