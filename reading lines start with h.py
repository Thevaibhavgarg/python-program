a=open("reading file.txt","r")
name1=a.readlines()
n=len(name1)
print(name1)
print("*"*10)
for i in range(n):
    b=name1[i]
    if(b[0]=="h" or b[0]=="H"):
             print(name1[i])
a.close()
