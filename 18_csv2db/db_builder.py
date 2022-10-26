#The Bottlers (Jeff Chen, Yusha Aziz, Fang Chen)
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#25 Oct 2022
#Time spent: 

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

if c.execute("select name from sqlite_schema where type = 'table'").fetchall() == []:

	tbleName = "courses"
	parameters = "code TEXT, mark INT, id INT"

	command = (f"create table {tbleName} ({parameters})")
	c.execute(command)

	with open("./courses.csv") as file:
		reader = csv.DictReader(file)
		for row in reader:
			code = row['code']
			mark = row['mark']
			id = row['id']
			command = (f"insert into courses values(\"{code}\", {mark}, {id})")
			c.execute(command)

print(c.execute('select * from courses').fetchall())

#==========================================================

db.commit() #save changes
db.close()  #close database


