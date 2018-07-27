import json
import socket
import ssl
from ast import literal_eval


class LoginError(Exception):
	pass

class ConnectionError(Exception):
	pass

class RequestError(Exception):
	pass

class Vndb():

	terminator = '\u0004'
	host = "api.vndb.org"
	port = 19534
	tls_port = 19535

	possible_flags = {
				"vn":["basic","details","anime","relations","tags","stats","screens","staff"],
				"release":["basic","details","vn"],
				"producer":["basic","details","relations"],
				"character":["basic","details","meas","traits","vns","voiced","instances"],
				"staff":["basic","details","aliases","vns","voiced"],
				"user":["basic"],
				"votelist":["basic"],
				"vnlist":["basic"],
				"wishlist":["basic"]
	}

	# TODO: Enforce filter checking

	def __init__(self):
		self.connected = False
		self.loggedin = False
		self.socket = None

	def open_connection(self,tls=True):
		sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
		if tls is True:
			port = Vndb.tls_port
			context = ssl.SSLContext()
		else:
			port = Vndb.port
		addr = (Vndb.host,port)
		if tls is True:
			SSLsock = context.wrap_socket(sock)
			self.socket = SSLsock
		else:
			self.socket = sock
		self.socket.connect(addr)
		return True

	def send(self,message):
		#TODO: implement write to api endpoint
		message += Vndb.terminator
		if self.connected is not True:
			raise LoginError(
				"You are not logged in\n"
				"This is necessary to access the database\n"
				"Calling Vndb.login() will successfully estabilish a limited connection as default"
				)
		message = str.encode(message)
		self.socket.send(message)
		res = self.socket.recv(4096)
		# Remove END OF TRANSMISSION and return string
		res = res.decode()[:-1]
		if res == 'ok':
			pass
		else:
			res = self.response_parser(res)
		return res

	def login(self,protocol=1,client='demo',clientver=0.1,username=None,password=None):
		if self.connected is not True:
			self.connected = self.open_connection()

		if username and password is not None:
			arg = {'protocol': protocol,
					'client': client, 'clientver': clientver,
		 			'username': username, 'password': password
		 			}
		else:
			arg = {'protocol': protocol,
					'client': client, 'clientver': clientver
		 			}

		message =  "login" + json.dumps(arg, separators=(',',':'))

		res = self.send(message)
		if res != 'ok':
			raise LoginError("There was an error logging into the database\n"
				"If you have provided a username and password, they were incorrect\n"
				"Calling Vndb.login() will successfully estabilish a limited connection as default"
				)
		self.loggedin = True
		print("Succesfully logged in")

	def logout(self):
		if not (self.loggedin or self.connected):
			raise LoginError(
				"You cannot logout if you are not logged in\n"
				"Please login before you try to logout"
				)
		self.socket.shutdown(socket.SHUT_RDWR)
		self.socket.close()
		self.connected = False
		self.loggedin = False

	def dbstats(self):
		message = "dbstats"
		res = self.send(message)
		return res

	def get(self,type,flags,filters,options):
		if isinstance(flags,str):
			flags = [flags]
		if not set(flags).issubset(Vndb.possible_flags[type]):
			raise RequestError("You have requested flags which do not existn\n"
				"To see all avaiable flags, Vndb.possible_flags returns a dictionary\n"
				"which can be indexed by the type of request, i.e Vndb.possible_flags[\"vn\"]"
				)
		if self.loggedin is not True:
			raise LoginError(
				"You are not logged in\n"
				"This is necessary to access the database\n"
				"Calling Vndb.login() will successfully estabilish a limited connection as default"
				)
		request = self.request_parser(flags,filters,options)
		message = "get " + type + request
		res = self.send(message)
		return res

	@staticmethod
	def request_parser(flags,filters,options):
		request = " "
		request += ",".join(flags)
		if filters:
			request += " ("
			for filter in filters:
				request += ",".join(filters)
			request += ") "
		if options:
			request += json.dumps(options)
		return request

	@staticmethod
	def response_parser(res):
		error_flag=False
		res = res.split(' ',1)
		if res[0] == 'error':
			error_flag = True
		res = (res[-1])
		# Gotta fix the non-parseable python things
		res = res.replace('false', 'False')
		res = res.replace('true', 'True')
		res = res.replace('null', 'None')
		res = literal_eval(res)
		# If error, return something slightly meaningful
		if error_flag:
			return res['id'].upper() + " error: Please refer to API documentation"
		# Remove square brackets around items value for requests with options
		if "items" in res.keys():
			res["items"]=res["items"][0]
			res = res["items"]
		return res

	def vn(self,flags=None,filters=None,options=None):
		res = self.get('vn',flags,filters,options)
		return res

	def release(self,flags=None,filters=None,options=None):
		res = self.get('release',flags,filters,options)
		return res

	def producer(self,flags=None,filters=None,options=None):
		res = self.get('producer',flags,filters,options)
		return res

	def character(self,flags=None,filters=None,options=None):
		res = self.get('character',flags,filters,options)
		return res

	def staff(self,flags=None,filters=None,options=None):
		res = self.get('staff',flags,filters,options)
		return res

	def user(self,flags=None,filters=None,options=None):
		res = self.get('user',flags,filters,options)
		return res

	def votelist(self,flags=None,filters=None,options=None):
		res = self.get('votelist',flags,filters,options)
		return res

	def vnlist(self,flags=None,filters=None,options=None):
		res = self.get('vnlist',flags,filters,options)
		return res

	def wishlist(self,flags=None,filters=None,options=None):
		res = self.get('wishlist',flags,filters,options)
		return res