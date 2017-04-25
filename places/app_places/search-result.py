import psycopg2

if input_text:
    try:
        conn = psycopg2.connect("dbname='app_places' user='bulikkk' host='localhost' password='qwer1234'")
    except:
        raise 'Error 1'

    cur = conn.cursor()

    try:
        cur.execute("""SELECT * from app_places_place WHERE """)
    except:
        raise 'Error 2'

    rows = cur.fetchall()

    return rows

