import sqlite3 as sql 

con = sql.connect ('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS tarefas')

sql = ''' CREATE TABLE "tarefas" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "TITULO" TEXT,
    "DESCRIÇÃO" TEXT,
    "DATA" TEXT,
    "STATUS" TEXT
    )'''
cur.execute(sql)
con.commit()
con.close()