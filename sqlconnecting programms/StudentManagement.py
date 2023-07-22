import os
import platform
from colorama import init
from colorama import Fore
init()
try:
	import mysql.connector as sql
except:
	os.system('pip install mysql-connector-python')
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')
	import mysql.connector as sql


con = sql.connect(
	host = "localhost",
	user = "root",
	passwd = "vaibhav",
	database = "test"
)


cursor = con.cursor()

def main():
	print(Fore.GREEN)
	print("""
	STUDENT MANAGEMENT SYSTEM
	
	1. View All Students
	2. Add a new Student
	3. Get Full Details of a Student
	4. Update a Record
	5. Delete a Student
	6. Exit  """)
	print(Fore.RESET)
	
	ch = int(input("Enter Your Choice: "))
	print(Fore.WHITE)
	if ch == 1:
		print("\n")
		cursor.execute("select * from studata")
		data = cursor.fetchall()
		for x in data:
			print(x[0], "\t", x[1])
		
	elif ch == 2:
		print("\n")
		cursor.execute("select roll from studata")
		rno = int(input("Enter Roll Number: "))
		for x in cursor.fetchall():
			if rno == x[0]:
				print(Fore.RED)
				print("Student Already Exist!!")
				break
		else:
			nm = input("Enter Name: ")
			gen = input("Enter Gender (M/F): ")
			per = float(input("Enter Percentage: "))
			mail = input("Enter email: ")
			try:
				st = "insert into studata values({}, '{}', '{}', {}, '{}')".format(rno, nm, gen, per, mail)
				cursor.execute(st)
				con.commit()
				print(Fore.GREEN)
				print("Student Added Successfully.")
			except:
				print(Fore.RED)
				print("An Error Occurred!!!")
		
	elif ch == 3:
		print("\n")
		inp = int(input("Enter Roll Number to Get Details: "))
		cursor.execute("select * from studata")
		data = cursor.fetchall()
		for x in data:
			if x[0] == inp:
				print("\nRoll No.: ", x[0])
				print("Name: ", x[1])
				print("Gender: ", x[2])
				print("Percentage: ", x[3])
				print("Email ID: ", x[4])
				break
		else:
			print(Fore.RED)
			print("Record Not Found!!!")
	
	elif ch == 4:
		roll = int(input("Enter Roll no To Update Record: "))
		cursor.execute("select * from studata")
		raw_data = cursor.fetchall()
		for x in raw_data:
			if x[0] == roll:
				print("Record Found for Roll No", roll)
				newname = input("Enter New Name: ")
				newgen = input("Enter New Gender [M/F]: ")
				newper = float(input("Enter New Percentage: "))
				newmail = input("Enter New E-mail: ")
				
				query = "update studata set name = '{}', gender = '{}', percent = {}, email = '{}' where roll = {}".format(newname, newgen, newper, newmail, roll)
				try:
					cursor.execute(query)
					con.commit()
					print(Fore.GREEN)
					print("Data Updated Successfully!")
				except:
					print(Fore.RED)
					print("An Error Occoured!!")
		
	elif ch == 5:
		print('\n')
		rno = int(input("Enter Roll No to Delete Record: "))
		query = "delete from studata where roll = {}".format(rno)
		print(Fore.RED)
		ch = input("Do You Really Want To Delete This Record (Y/N)? ")
		if ch.lower() == 'y':
			try:
				cursor.execute(query)
				con.commit()
				print(Fore.GREEN)
				print("Data Deleted Successfully.")
			except:
				print(Fore.RED)
				print("An Error Occurred!!!")
		else:
			pass
	
		
	elif ch == 6:
		exit()
	else:
		print(Fore.RED)
		print("Invalid Choice!!!")
	
	print(Fore.RESET)
	loop = input("\nRun Again (Y/N)? ")
	if loop.lower() == 'y':
		os.system('cls')
		main()
	else:
		exit()

main()
