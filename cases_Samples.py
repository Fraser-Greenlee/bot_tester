# -*- coding: utf-8 -*-

'''
	Sample Cases file
'''

import web
import testbot

# set url
testbot.send_to = 'http://0.0.0.0:8080/webhook'
# using local database
db = web.database(dbn='postgres',db='secret',user='postgres',pw='',host='localhost')

## Required
# will be called from app.py at start
def run():
	results = []
	clear_tables()

	results.append(new_user())
	clear_tables()

	# define test users
	users = []
	for id in [1,2,3,4,5]:
		u = testbot.User(id)
		u.postback("GetStarted")
		users.append(u)
	#
	results += err_len(users)
	#
	testbot.results(results)

# Tools

def clear_tables():
	db.query("delete from users")
	db.query("delete from messages")
	testbot.clear_messages()

## Test Cases

def new_user():
	user = testbot.User()
	user.postback("GetStarted")
	return user.did_receive("Welcome to Tweet bot. Post your messages bellow.")

def err_len(users):
	# Test multiple responces from same issue
	r = []
	users[0].send("a"*201)
	r.append(users[0].did_receive("Not Sent\nMust be under 200 characters."))
	users[0].send("a"*201)
	r.append(users[0].did_receive("Still too long.\nTry removing emojis."))
	return r
