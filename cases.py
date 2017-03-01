# -*- coding: utf-8 -*-
import web, os, shutil
import testbot

db = web.database(dbn='postgres',db='secret',user='postgres',pw='',host='localhost')

def run():
	results = []
	clear_tables()
	#
	results.append(new_user())
	clear_tables()

	# define test users
	users = []
	for id in [1,2,3,4,5]:
		u = testbot.User(id)
		u.postback("GetStarted")
		users.append(u)
	#
	results += error_handles(users)

	print ''
	print results
	print ''
	for res in results:
		if res[0]:
			print 'PASSED:', res[1]
		else:
			print 'FAILED. Expected:', res[1], ' Got:', res[2]

###

def clear_tables():
	db.query("delete from users")
	db.query("delete from messages")
	if os.path.exists('messages'):
		shutil.rmtree('messages')

def last_msg(user,equals):
	try:
		l = user.last_msg()['message']['text']
	except:
		print 'WARNING: last_msg does not have text'
		return testbot.test( "$Error: non text message." , equals)
	return testbot.test( l[l.index(' ')+1:] , equals)

###

def new_user():
	user = testbot.User()
	user.postback("GetStarted")
	return user.did_receive("🐧 Welcome to Floc.\nA place for anonymous group chats on Messenger.")

#

def error_handles(users):
	r = []
	r += err_len(users)
	r += err_newlines(users)
	return r

def err_len(users):
	r = []
	users[0].send("a"*201)
	r.append(users[0].did_receive("🐧 Not Sent\nMust be under 200 characters."))
	users[0].send("a"*201)
	r.append(users[0].did_receive("🐧 Still too long.\nTry removing emojis."))
	users[0].send("x")
	r.append(last_msg(users[1], "x"))
	return r

def err_newlines(users):
	r = []
	users[0].send('\n'*5)
	r.append(users[0].did_receive("🐧 Not Sent\nMust have less than 5 newline characters."))
	users[0].send('\n'*5)
	r.append(users[0].did_receive("🐧 Still too many."))
	users[0].send("x")
	r.append(last_msg(users[1], "x"))
	return r
