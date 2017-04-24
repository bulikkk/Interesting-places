import psycopg2

try:
    conn = psycopg2.connect("dbname='app_places' user='bulikkk' host='localhost' password='qwer1234'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

cur.execute("""SELECT * from app_places_place""")
