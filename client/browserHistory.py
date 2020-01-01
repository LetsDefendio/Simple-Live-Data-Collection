import os
import getpass 
import sqlite3


username = getpass.getuser()
directory = ""
path = os.path.expanduser('~')+"/.mozilla/firefox/"
files = os.listdir(path)


for name in files:
	if ".default" in name:
		directory = name


data_path = os.path.expanduser('~')+"/.mozilla/firefox/"+directory
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'places.sqlite')
c = sqlite3.connect(history_db)
cursor = c.cursor()
select_statement = "select moz_places.url, moz_places.visit_count from moz_places;"
cursor.execute(select_statement)
results = cursor.fetchall()


for url, count in results:
	print(url)