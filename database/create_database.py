#5.sep.2025

#username (id), password (encrypted), date of creation utc year/mounch/day/time,location (ip),browser,notes



import sqlite3


con = sqlite3.connect("data1.db")


cursor = con.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS data1 (
               id TEXT PRIMARY KEY,
               pcontact TEXT NOT NULL,
               domain TEXT,
               notes TEXT, 
               contact2 TEXT,
               contact3 TEXT,
               date TEXT NOT NULL,
               creator TEXT NOT NULL,
               password TEXT NOT NULL
)            
''')


cursor.execute("INSERT INTO data1 (id,pcontact,domain,notes,date,creator,password) VALUES ('haywik','nobodysgamer11@gmail.com','haywik.com','first account','2025/SEPTEMBER/5/1950','haywik','12345') ")

con.commit()

print("Data base created..")