from user import User
from recieve import recieve

def test(got, expected):
	if expected == got:
		return [True, expected.replace('\n',' \ ')]
	else:
		return [False, expected, got]
