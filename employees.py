class employees:
	emp_id=""
	emp_name=""
	emp_gender=""
	emp_city=""
	emp_salary=0
	def emp_data(self):
		self.emp_id=input("Enter emp id:")
		self.emp_name=input("Enter emp name:")
		self.emp_gender=input("Enter emp gender:")
		self.emp_city=input("Enter emp city:")
		self.emp_salary=input("Enter emp salary")
	def emp_display(self):
		print("emp_id:",self.emp_id)
		print("emp_name:",self.emp_name)
		print("emp_gender:",self.emp_gender)
		print("emp_city:",self.emp_city)
		print("emp_salary:",self.emp_salary)
#main()
n=int(input("Enter no. of entries:"))
for i in range(n):
      emp=employees()
      emp.emp_data()
      emp.emp_display()
      print("*"*10)