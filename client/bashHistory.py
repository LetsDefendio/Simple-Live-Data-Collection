import os

homedir = os.path.expanduser('~')
history = open(homedir+"/.bash_history", 'r')

for i in history:
	print(i)
