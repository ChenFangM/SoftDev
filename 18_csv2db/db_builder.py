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


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
with open("./courses.csv",) as file:
    reader = csv.DictReader(file)

c.execute("select name from sqlite_master")
tables = c.fetchall();
if "courses" not in tables:
    command = "create table courses(code text, mark int, id int)"   #test SQL stmt in sqlite3 shell, save as string
    c.execute(command)    # run SQL statement
#==========================================================

db.commit() #save changes
db.close()  #close database


