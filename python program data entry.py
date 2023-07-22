a=open("python program.txt","w")
for i in range (3):
	x=input("ENTER NAME:")
	a.write(x)
	a.write("\n")
a.close()
a=open("python program.txt","r")
name1=a.readlines()
for i in range(3):
	print(name1[i])
a.close()