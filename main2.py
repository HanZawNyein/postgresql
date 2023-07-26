import psycopg2

try:
    conn = psycopg2.connect(dbname="odoo16c_2", user="odoo", password="odoo")
    cur = conn.cursor()
    cur.execute("select id,login,password from res_users order by id;")
    results = cur.dict()
    for res in results:
        print(res)
except Exception as e:
    print(e)