#import requests
import json

class Vndb():

	terminator = '\u0004'

	def __init__():
		pass

	def send():
		#TODO: implement write to api endpoint
		pass

	def login(self,protocol=1,client='demo',clientver=0.1,username=None,password=None):
		
		arg = {'protocol': protocol,
		'client': client, 'clientver': clientver,
		 'username': username, 'password': password}

		message =  "login" + json.dumps(arg, separators=(',',':')) + Vndb.terminator

		res = self.send(message)
		return res.json()

	def dbstats(self):
		message = "dbstats"
		res = self.send(message)
		return res.json()

	def get(self,type=None,flags=None,filters=None,options=None):
		request = self.request_parser(flags,filters,options)
		message = "get" + "type" + request
		res = self.send(message)
		return res

	def request_parser():
		#TODO: Implement request parser
		pass

	def vn(self,flags,filters,options):
		res = self.get('vn',flags,filters,options)
		return res.json()

	def releases(self,flags,filters,options):
		res = self.get('releases',flags,filters,options)
		return res.json()

	def producer(self,flags,filters,options):
		res = self.get('producer',flags,filters,options)
		return res.json()

	def character(self,flags,filters,options):
		res = self.get('character',flags,filters,options)
		return res.json()

	def staff(self,flags,filters,options):
		res = self.get('staff',flags,filters,options)
		return res.json()

	def user(self,flags,filters,options):
		res = self.get('user',flags,filters,options)
		return res.json()

	def votelist(self,flags,filters,options):
		res = self.get('votelist',flags,filters,options)
		return res.json()

	def vnlist(self,flags,filters,options):
		res = self.get('vnlist',flags,filters,options)
		return res.json()

	def wishlist(self,flags,filters,options):
		res = self.get('wishlist',flags,filters,options)
		return res.json()