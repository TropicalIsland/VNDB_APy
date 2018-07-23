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

	def get(self,type,request=None):
		message = "get" + "type" + request
		res = self.send(message)
		return res

	def request_parser():
		pass

	def vn(self,flags,filters,options):
		request = self.request_parser(flags,filters,options)
		res = self.get('vn',request)
		return res.json()

	def releases(self,flags,filters,options):
		request = self.request_parser(flags,filters,options)
		res = self.get('releases',request)
		return res.json()

	def producer(self,flags,filters,options):
		request = self.request_parser(flags,filters,options)
		res = self.get('producer',request)
		return res.json()

	def character(self,flags,filters,options):
		request = self.request_parser(flags,filters,options)
		res = self.get('character',request)
		return res.json()

	def staff(self,flags,filters,options):
		request = self.request_parser(flags,filters,options)
		res = self.get('staff',request)
		return res.json()

	def user(self,flags,filters,options):
		request = self.request_parser(flags,filters,options)
		res = self.get('user',request)
		return res.json()

	def votelist(self,flags,filters,options):
		request = self.request_parser(flags,filters,options)
		res = self.get('votelist',request)
		return res.json()

	def vnlist(self,flags,filters,options):
		request = self.request_parser(flags,filters,options)
		res = self.get('vnlist',request)
		return res.json()

	def wishlist(self,flags,filters,options):
		request = self.request_parser(flags,filters,options)
		res = self.get('wishlist',request)
		return res.json()