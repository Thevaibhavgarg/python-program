a=open("reading file.txt","r")
#to display the file
q=a.read()
print(q)
a.seek(0)
print("*"*30)
#main program
z=a.readlines()
size=0
wsize=0
for i in z:
	size=size+len(i)
	wsize=wsize+len(i.split())
print("total charactar is:",size)
print("total word is:",wsize)