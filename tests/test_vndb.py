from vndbwrapper import Vndb
from pytest import fixture
import sys

@fixture
def stats_keys():
	return ["users", "threads", "tags", "releases", 
    "producers", "chars", "posts", "vn", "traits"
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
def test_flags():
	return ["id","msg"]

@fixture
def test_filters():
	return ["id","msg"]

@fixture
def test_options():
	return {"page":2,"results":2,"sort":"id","reverse":True}


# TODO: Modularise the testing
def test_request_paser():
	Vndb_instance = Vndb()
	Vndb_instance.request_parser(flags=["basic","details"],filters=["id = 7"],options={"reverse":True})

def test_vndb_wrapper():
	"""Tests several API GET calls to VNDB"""
	Vndb_instance = Vndb()
	# Login check, necessary for all further connections
	Vndb_instance.login()

	# Check dbstats
	res = Vndb_instance.dbstats()
	print(res)
	assert isinstance(res, dict)
	assert set(stats_keys()).issubset(res.keys())

	# Check VN
	res = Vndb_instance.vn(flags=["basic","details"],filters=["id = 7"],options={"reverse":True})
	assert isinstance(res, dict)
	assert set(vn_keys()).issubset(res["items"].keys())

	# Check release
	res = Vndb_instance.release()
	print(res)
	assert isinstance(res, dict)
	assert set(release_keys()).issubset(res.keys())

	# Check producer
	res = Vndb_instance.producer()
	print(res)
	assert isinstance(res, dict)
	assert set(producer_keys()).issubset(res.keys())

	# Check character
	res = Vndb_instance.character()
	print(res)
	assert isinstance(res, dict)
	assert set(character_keys()).issubset(res.keys())

	# Check staff
	res = Vndb_instance.staff()
	print(res)
	assert isinstance(res, dict)
	assert set(staff_keys()).issubset(res.keys())

	# Check user
	res = Vndb_instance.user()
	print(res)
	assert isinstance(res, dict)
	assert set(user_keys()).issubset(res.keys())

	# Check votelist
	res = Vndb_instance.votelist()
	print(res)
	assert isinstance(res, dict)
	assert set(votelist_keys()).issubset(res.keys())

	# Check VNlist
	res = Vndb_instance.vnlist()
	print(res)
	assert isinstance(res, dict)
	assert set(vnlist_keys()).issubset(res.keys())

	# Check Wishlist
	res = Vndb_instance.wishlist()
	print(res)
	assert isinstance(res, dict)
	assert set(wishlist_keys()).issubset(res.keys())

	# Check Error Response
	res = Vndb_instance.vn('wrong')
	print(res)
	assert isinstance(res, dict)
	assert set(error_keys()).issubset(res.keys())

	# Check logout
	# Vndb_instance.close()