# mini web.py app for hosting alternative server
from multiprocessing import Process
import web, testbot, json
import cases

urls = (
		'/.*', 'main'
)
app = web.application(urls, globals())

class main:
	def GET(self):
		# shouldn't send get
		return 'Error: should not reieve GET request'
	def POST(self):
		# revieve message
		print web.data()
		# add message to txt file
		return testbot.recieve(web.data())

if __name__ == "__main__":
  p1 = Process(target=web.httpserver.runsimple, args=(app.wsgifunc(), ("0.0.0.0", 8888)))
  p1.start()
  p2 = Process(target=cases.run)
  p2.start()
  p1.join()
  p2.join()
