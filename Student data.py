class student:
	stu_id=0
	stu_name=""
	s1=0
	s2=0
	s3=0
	total=0
	per=0
	def stu_data(self):
		self.stu_id=input("Enter student id:")
		self.stu_name=input("Enter student name:")
		self.s1=int(input("Enter s1 marks:"))
		self.s2=int(input("Enter s2 marks:"))
		self.s3=int(input("Enter s3 marks:"))
	def stu_cal(self):
		self.total=self.s1+self.s2+self.s3
		self.per=self.total/3
	def stu_display(self):
		print("stu_id:",self.stu_id)
		print("stu_name:",self.stu_name)
		print("s1 marks:",self.s1)
		print("s2 marks:",self.s2)
		print("s3 marks:",self.s3)
		print("total marks:",self.total)
		print("percentage:",self.per,"%")
#main()
n=int(input("Enter no. of entries:"))
for i in range(n):
      stu=student()
      stu.stu_data()
      stu.stu_cal()
      stu.stu_display()
      print("*"*10)