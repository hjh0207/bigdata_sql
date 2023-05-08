import sqlite3


con = sqlite3.connect('dbdb.db')
cursor = con.cursor() # sql 문장을 실행시키기 위해 준비

sql = '''
INSERT INTO Person (ID, Name, Birthday)
VALUES (1, '이혜리', '1994-06-09');
'''
cursor.execute(sql) # sql 을 실행
con.commit()
con.close()