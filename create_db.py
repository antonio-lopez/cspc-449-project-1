import sqlite3

conn = sqlite3.connect('redditDB.db')
c = conn.cursor()

conn.execute('''CREATE TABLE userpost_tbl
         (postId INTEGER PRIMARY KEY UNIQUE,
         title  TEXT   NOT NULL,
         text   TEXT   NOT NULL,
         community  TEXT   NOT NULL,
         url    TEXT,
         username   TEXT   NOT NULL,
         date   TEXT    NOT NULL);''')

conn.execute('''CREATE TABLE user_tbl
         (username  TEXT   NOT NULL UNIQUE,
         email  TEXT NOT NULL UNIQUE,
         karma  INTEGER NOT NULL);''')

print("Database created successfully")

conn.commit()

conn.close()