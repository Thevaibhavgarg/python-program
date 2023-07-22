import mysql.connector as m

con = m.connect(host = "localhost",
	user = "root", passwd = "vaibhav",
	database = "sakila"
	)
cursor = con.cursor()
cursor.execute('select * from city')

data = cursor.fetchall()
for x in data:
	print(x)
