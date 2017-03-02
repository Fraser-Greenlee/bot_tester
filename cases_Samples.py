# -*- coding: utf-8 -*-
import web, time
import testbot

testbot.send_to = 'http://0.0.0.0:8080/webhook'
db = web.database(dbn='postgres',db='secret',user='postgres',pw='',host='localhost')

def run():
	results = []
	clear_tables()
	#
	results.append(new_user())
	#
	testbot.results(results)

## Tools

def clear_tables():
	db.query("delete from users")
	db.query("delete from messages")
	testbot.clear_messages()

def get_users():
	users = []
	for id in [1,2,3,4,5]:
		u = testbot.User(id)
		u.postback("GetStarted")
		users.append(u)
	return users

## Test Cases

def new_user():
	user = testbot.User()
	user.postback("GetStarted")
	return user.did_receive("Welcome to Tweet bot. Post your messages bellow.")
