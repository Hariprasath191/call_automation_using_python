import psycopg2

conn = psycopg2.connect(
    host="209.182.232.150",
    port="5432",
    database="igxerp2024",
    user="igxerp",        # or the actual DB username
    password="igxerp"
)
cursor = conn.cursor()
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
rows = cursor.fetchall()
print(rows)

cursor.close()
conn.close()
