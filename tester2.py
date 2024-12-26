import psycopg2

def update_database(data):
    # 데이터베이스에 연결
    conn = psycopg2.connect("dbname=test user=postgres password=secret")
    cur = conn.cursor()
    # 데이터를 업데이트
    cur.execute("INSERT INTO solar_data (timestamp, value) VALUES (NOW(), %s)", (data['value'],))
    conn.commit()
    cur.close()
    conn.close()

data = {'value':-99}
update_database(data)