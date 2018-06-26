#Q1
import sqlite3
conn=sqlite3.connect('books.db')
print("Database Created")
conn.execute('''CREATE TABLE BOOKS (BOOK_ID INT PRIMARY KEY NOT NULL,
TITLE_ID TEXT NOT NULL,
LOCATION TEXT NOT NULL,
GENRE TEXT NOT NULL);''')
conn.execute('''CREATE TABLE TITLE (TITLE_ID INT NOT NULL,
TITLE_NAME TEXT NOT NULL,
ISBN INT NOT NULL,
PUBLISHER_ID INT NOT NULL,
PUBLISHER_YEAR INT NOT NULL);''')

conn.execute('''CREATE TABLE PUBLISHERS(PUBLISHER_ID INT NOT NULL,
NAME TEXT NOT NULL,
STREET_ADDRESS CHAR(50),
SUITE_NUMBER INT NOT NULL,
ZIP_CODE_ID INT NOT NULL);''')

conn.execute('''CREATE TABLE ZIPCODES (ZIP_CODE_ID INT NOT NULL,
CITY TEXT NOT NULL,
STATE TEXT NOT NULL,
ZIP_CODE INT NOT NULL);''')

conn.execute('''CREATE TABLE AUTHORSTITLES (AUTHORS_TITLES_ID INT NOT NULL,
AUTHOR_ID INT NOT NULL,
TITLE_ID INT NOT NULL);''')

conn.execute('''CREATE TABLE AUTHORS (AUTHOR_ID INT PRIMARY KEY NOT NULL,
FIRST_NAME TEXT NOT NULL,
MIDDLE_NAME TEXT NOT NULL,
LAST_NAME TEXT NOT NULL);''')
print("Table Created Successfully")
#Q2
conn.execute("INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE) VALUES(11023,25893,'INDIA','SCIENCE')")
conn.commit()
print("inserted successfully")

#Q3
conn.execute("INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE) VALUES(11023,25893,'DELHI','SCIENCE')")
conn.commit()
print("inserted successfully")

#Q3
print("Before Updation")
cusor=conn.execute("SELECT book_id,title_id,location,genre from books")
for row in cusor:
    print("BOOK_ID=",row[0])
    print("TITLE_ID=",row[1])
    print("LOCATION=",row[2])
    print("GENRE=",row[3],"\n")

print("AFTER UPDATING")
conn.execute("UPDATE BOOKS set TITLE_ID=55555 where BOOK_ID=11023")
cusor=conn.execute("SELECT book_id,title_id,location,genre from books")
for row in cusor:
    print("BOOK_ID=",row[0])
    print("TITLE_ID=",row[1])
    print("LOCATION=",row[2])
    print("GENRE=",row[3],"\n")
print("records created successfully")