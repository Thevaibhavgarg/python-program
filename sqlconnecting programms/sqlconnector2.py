import mysql.connector as m

con = m.connect(host = "localhost",
	user = "root", passwd = "vaibhav",
	database = "emp"
	)
cursor = con.cursor()
st="insert into empdata values({},'{}','{}')".format(1004,'aman','CA')
cursor.execute(st)
con.commit()
cursor.execute("select * from empdata")
data = cursor.fetchall()
for x in data:
	print(x)

