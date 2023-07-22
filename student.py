a=open("student.txt","w+")
for i in range (5):
	b=input("ENTER STUDENT NAME:")
	a.write(b)
	a.write("\n")
a.seek(0)
c=a.read()
print(c)