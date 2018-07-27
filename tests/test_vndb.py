from vndbwrapper import Vndb
from pytest import fixture

@fixture
def stats_keys():
	return ["users", "threads", "tags", "releases", 
    "producers", "staff","chars", "posts", "vn", "traits"
    ]

@fixture
def vn_keys():
 	return ["id", "title", "original", "released", 
 	"languages", "orig_lang", "platforms", "aliases", "length", 
 	"description", "links", "image", "image_nsfw", "anime", "relations", 
 	"tags", "popularity", "rating", "votecount", "screens", "staff"
 	]

@fixture
def release_keys():
 	return ["id", "title", "original", "released", 
 	"type", "patch", "freeware", "doujin", "languages", 
 	"website", "notes", "minage", "gtin", "catalog", "platforms", 
 	"media", "resolution", "voiced", "animation", "vn", "producers"
 	]

@fixture
def producer_keys():
 	return ["id", "name", "original", "type", 
    "language", "links", "aliases", "description", "relations"
    ]

@fixture
def character_keys():
 	return ["id", "name", "original", "gender", "bloodt", "birthday", 
 	"aliases", "description", "image", "bust", "waist", "hip", "height", 
 	"weight", "traits", "vns", "voiced", "instances"
 	]

@fixture
def staff_keys():
 	return ["id", "name", "original", "gender", "language", "links", 
 	"description", "aliases", "main_alias", "vns", "voiced"
 	]

@fixture
def user_keys():
 	return ["id", "username"
 	]

@fixture
def votelist_keys():
	return ["uid", "vn", "vote", "added"
	]

@fixture
def vnlist_keys():
	return ["uid", "vn", "status", "added", "notes"
	]

@fixture
def wishlist_keys():
	return ["uid", "vn", "priority", "added"
	]

@fixture
def error_keys():
	return ["id","msg"]

@fixture
def error_ids():
	return ["parse","missing","badarg","needlogin","throttled","auth",
	"loggedin","gettype","getinfo","filter","settype"]

@fixture
def test_flags():
	return ["basic"]

@fixture
def test_filters():
	return ["id >= 12"]

@fixture
def test_options():
	return {"page":2,"results":2,"sort":"id","reverse":True}


def test_request_paser():
	Vndb_instance = Vndb()
	req = Vndb_instance.request_parser(flags=test_flags(),filters=test_filters(),options=test_options())
	assert req == " basic (id >= 12) {\"page\": 2, \"results\": 2, \"sort\": \"id\", \"reverse\": true}"

def test_response_parser():
	Vndb_instance = Vndb()
	test = Vndb_instance.response_parser("results {\"items\": [{\"id\":3}]}")
	assert test == {"id": 3}

def _test_dbstats(Vndb):
	res = Vndb.dbstats()
	print(res)
	assert isinstance(res, dict)
	assert set(res).issubset(set(stats_keys()))

def _test_vn(Vndb):
	res = Vndb.vn(flags=test_flags(),filters=test_filters(),options=test_options())

	assert isinstance(res, dict)
	assert set(res.keys()).issubset(set(vn_keys()))

def _test_release(Vndb):
	res = Vndb.release(flags=test_flags(),filters=test_filters())
	print(res)
	assert isinstance(res, dict)
	set(res).issubset(set(release_keys()))

def _test_producer(Vndb):
	res = Vndb.producer(flags=test_flags(),filters=test_filters(),options=test_options())
	print(res)
	assert isinstance(res, dict)
	set(res).issubset(set(producer_keys()))

def _test_character(Vndb):
	res = Vndb.character(flags=test_flags(),filters=test_filters())
	print(res)
	assert isinstance(res, dict)
	set(res).issubset(set(character_keys()))

def _test_staff(Vndb):
	res = Vndb.staff(flags=test_flags(),filters=test_filters(),options=test_options())
	print(res)
	assert isinstance(res, dict)
	set(res).issubset(set(staff_keys()))

def _test_user(Vndb):
	res = Vndb.user(flags=test_flags())
	print(res)
	assert isinstance(res, dict)
	set(res).issubset(set(user_keys()))

def _test_votelist(Vndb):
	res = Vndb.votelist(flags=test_flags())
	print(res)
	assert isinstance(res, dict)
	set(res).issubset(set(votelist_keys()))

def _test_vnlist(Vndb):
	res = Vndb.vnlist(flags=test_flags(),filters=test_filters())
	print(res)
	assert isinstance(res, dict)
	set(res).issubset(set(vnlist_keys()))

def _test_wishlist(Vndb):
	res = Vndb.wishlist(flags=test_flags())
	print(res)
	assert isinstance(res, dict)
	set(res).issubset(set(wishlist_keys()))


def test_vndbwrapper():
	"""Tests entire wrapper functionality"""
	Vndb_instance = Vndb()

	# Login check, necessary for all further connections
	Vndb_instance.login()

	_test_dbstats(Vndb_instance)
	_test_vn(Vndb_instance)
	_test_release(Vndb_instance)
	_test_producer(Vndb_instance)
	_test_character(Vndb_instance)
	_test_staff(Vndb_instance)

	## These return a parse error for basic?
	## Invalid arguments to get command
	#test_user(Vndb_instance)
	#test_votelist(Vndb_instance)
	#test_vnlist(Vndb_instance)
	#test_wishlist(Vndb_instance)

	# Check logout
	Vndb_instance.logout()
