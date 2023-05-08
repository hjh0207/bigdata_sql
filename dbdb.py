import sqlite3

# 연결
def db_con():
    return sqlite3.connect('dbdb.db')

# 데이터 넣기
def save_data():
    con = db_con()
    cursor = con.cursor()
    sql = '''
    INSERT INTO Person (ID, Name, Birthday)
    VALUES (1, '이혜리', '1994-06-09');
    '''
    cursor.execute(sql) # sql 을 실행
    con.commit()
    con.close()

#데이터 보기 함수
def get_data():
    sql = '''
    SELECT * FROM Person;
    '''
    cursor.execute(sql) # sql 을 실행
    #data = cursor.fetchone()
    #print(data)

    all_data = cursor.fetchall()
    print(all_data)