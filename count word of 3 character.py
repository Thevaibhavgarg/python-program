a=open("reading file.txt","r")
#to display the file
q=a.read()
print(q)
a.seek(0)
print("*"*30)
#main program
z=a.readlines()
size=0
for i in z: #acees one line in i as a string
    q=i.split() # acess words of the line
    for j in q: # acess one word of the line
            if len(j)==3:
                print(j)
                size=size+1
print("total charactar is:",size)
