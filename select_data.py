import sqlite3


con = sqlite3.connect('dbdb.db')
cursor = con.cursor() # sql 문장을 실행시키기 위해 준비

sql = '''
SELECT * FROM Person;
'''
cursor.execute(sql) # sql 을 실행
#data = cursor.fetchone()
#print(data)

all_data = cursor.fetchall()
print(all_data)