#print fibonacci series
a=int(input("Enter the limit:"))
x=0
y=1
z=1
print("fibonacci series")
print(x,y,end=" ")
while(z<=a):
    print(z,end=" ")
    x=y
    y=z
    z=x+y
