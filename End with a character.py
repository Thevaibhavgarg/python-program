a=open("python program.txt","r")
#to display the file
q=a.read()
print(q)
a.seek(0)
print("*"*30)
#main program
z=a.readlines()
for i in z:
	x=i.split()
	w=x[-1]
	if(w[-1]=="a"or w[-1]=="A"):
		print(i)