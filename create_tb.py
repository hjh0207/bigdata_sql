import sqlite3


con = sqlite3.connect('dbdb.db')
cursor = con.cursor() # sql 문장을 실행시키기 위해 준비

sql = '''
CREATE TABLE "melon" (
    "rank"    INTEGER NOT NULL,
    "title"  TEXT NOT NULL,
    "artist"  TEXT NOT NULL,
    PRIMARY KEY("rank" AUTOINCREMENT)
)
'''
cursor.execute(sql) # sql 을 실행
con.commit()
con.close()