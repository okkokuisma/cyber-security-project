import sqlite3

def create_aphorism(text):
  con = sqlite3.connect('db.sqlite3')
  cur = con.cursor()
  sql = "INSERT INTO app_aphorism (aphorism_text) VALUES ('%s');" % (text)
  print(sql)
  cur.execute(sql)
  con.commit()
  con.close()