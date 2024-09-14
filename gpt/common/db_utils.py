import cx_Oracle

def read_sql_query(sql):
    print(sql)
    try:
        dsn = cx_Oracle.makedsn('192.168.61.5', '1521', sid='uat')
        conn = cx_Oracle.connect(user='flexion', password='flexion', dsn=dsn)
        cur = conn.cursor()
        cur.execute(sql)
        column_names = [col[0] for col in cur.description]
        print(column_names)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return [column_names,rows]
    except cx_Oracle.DatabaseError as e:
        print(f"Database error: {e}")
        return "DB_ERROR"