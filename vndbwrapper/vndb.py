#import requests
import json
import socket
import ssl


def LoginError(Exception):
	pass

def ConnectionError(Exception):
	pass

class Vndb():

	terminator = '\u0004'
	host = "api.vndb.org"
	port = 19534
	tls_port = 19535

	def __init__(self):
		self.connected = False
		self.loggedin = False
		self.socket = None

	def open_connection(self,tls=True):
		sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
		if tls is True:
			port = Vndb.tls_port
			context = ssl.SSLcontext()
		else:
			port = Vndb.port
		addr = (Vndb.host,port)
		if tls is True:
			SSLsock = context.wrap_socket(sock)
			self.socket = SSLsock
		else:
			self.socket = sock
		sock.connect(addr)
		return True

	def send(self,message):
		#TODO: implement write to api endpoint
		if self.loggedin is not True:
			raise LoginError(
				"You are not logged in"
				"This is necessary to access the database"
				"Calling Vndb.login() will successfully estabilish a limited connection as default"
				)
		self.socket.send(message)
		pass

	def login(self,protocol=1,client='demo',clientver=0.1,username=None,password=None):

		if self.connected is not True:
			self.open_connection()

		arg = {'protocol': protocol,
		'client': client, 'clientver': clientver,
		 'username': username, 'password': password}

		message =  "login" + json.dumps(arg, separators=(',',':')) + Vndb.terminator

		res = self.send(message)
		if res is not "OK":
			raise LoginError(
				"There was an error logging into the database"
				"If you have provided a username and password, they were incorrect"
				"Calling Vndb.login() will successfully estabilish a limited connection as default"
				)
		self.loggedin = True
		print("Succesfully logged in")

	def logout(self):
		self.socket.shutdown()
		self.socket.close()

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