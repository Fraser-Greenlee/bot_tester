import os, shutil
from user import User
from recieve import recieve

# Default values
send_to = 'http://0.0.0.0:8080/webhook'
page_id = 1

# tools
def test(got, expected):
	if expected == got:
		return [True, expected.replace('\n',' \ ')]
	else:
		return [False, expected, got]

def clear_messages():
	if os.path.exists('messages'):
		shutil.rmtree('messages')

def results(ress):
		print ''
		print 'RESULTS'
		print '-------'
		for res in ress:
			if res[0]:
				print 'PASSED:', res[1]
			else:
				print 'FAILED'
				print 'Expected:', res[1], ' Got:', res[2]
