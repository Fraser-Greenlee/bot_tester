from os import listdir, makedirs
from os.path import isfile, join, exists
import json, requests, random, string, time

def getusers():
	return [int(f[:f.index('.')]) for f in listdir('messages/')]

def new_json_file(id):
	print 'new', str(id)+'.json'
	open('messages/'+str(id)+'.json', 'w').write(json.dumps({'checked_last':False,'messages':[]}))
	time.sleep(1)

def random_id():
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

def timestamp():
	return int(time.time()*(10**6))


class User:
	def __init__(self,*id):
		if not exists('messages/'):
			makedirs('messages/')
		#
		self.url = 'http://0.0.0.0:8080/webhook'
		self.page_id = 1
		#
		if len(id) is 0:
			# random new id
			users = getusers()
			id = 1
			while id in users:
				id+=1
			self.id = id
			print 'x', id
			new_json_file(id)
		else:
			# assign set id
			id = id[0]
			self.id = id
			if id not in getusers():
				print 'y', id
				new_json_file(id)

	def read(self):
		return json.load(open('messages/'+str(self.id)+'.json','r'))

	def write(self,data):
		open('messages/'+str(self.id)+'.json', 'w').write(json.dumps(data))

	def checked_last(self):
		return self.read()['checked_last']

	def messages(self):
		return self.read()['messages']

	def last_msg(self):
		return self.messages()[-1]

	def did_receive(self,msg):
		time.sleep(1)
		if self.checked_last():
			return [False, msg, '$Nothing New']
		if len(self.messages()) is 0:
			return [False, msg, '$Nothing']
		try:
			last_msg = self.messages()[-1]['message']['text']
			res = (unicode(msg, 'utf-8') == last_msg)
		except Exception as e:
			print 'Last Message Error:', str(e)
			res = False
			last_msg = '$Err: User has no messages.'
		data = self.read()
		data['checked_last'] = True
		self.write(data)
		if res is False:
			return [False, msg, last_msg]
		else:
			return [True, msg.replace('\n',' \ ')]

	def postback(self,key):
		requests.post(
			self.url,
			json={
				"object":"page",
				"entry":[
					{
						"id": self.page_id,
						"time":timestamp(),
						"messaging":[
							{
								"sender":{
									"id":self.id
								},
								"recipient":{
									"id": self.page_id
								},
								"timestamp":timestamp(),
							  "postback":{
							    "payload":key
							  }
							}
						]
					}
				]
			})
	#

	def send(self,data,**qs):
		if 'type' not in qs:
			type = 'text'
		else:
			type = qs['type']
		#
		if type == 'text':
			requests.post(
				self.url,
				json={
				  "object":"page",
				  "entry":[
				    {
				      "id": self.page_id,
				      "time":timestamp(),
				      "messaging":[
				        {
				          "sender":{
				            "id":self.id
				          },
				          "recipient":{
				            "id": self.page_id
				          },
									"timestamp":timestamp(),
								  "message":{
								    "mid":"mid."+str(timestamp())+":"+random_id(),
								    "text":data
									}
				        }
				      ]
				    }
				  ]
				})
		else:
			requests.post(
				self.url,
				json={
				  "object":"page",
				  "entry":[
				    {
				      "id": self.page_id,
				      "time":timestamp(),
				      "messaging":[
				        {
				          "sender":{
				            "id":self.id
				          },
				          "recipient":{
				            "id": self.page_id
				          },
									"timestamp":timestamp(),
								  "message":{
								    "mid":"mid."+str(timestamp())+":"+random_id(),
							        "attachments":[
																      {
																        "type":"image",
																        "payload":{
																          "url":data
																        }
																      }
																    ]
									}
				        }
				      ]
				    }
				  ]
				})
#
