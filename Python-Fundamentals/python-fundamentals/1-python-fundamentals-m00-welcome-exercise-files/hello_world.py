import sys

def hello(who):
	print('Hello {}'.format(who))

hello(sys.argv[1])