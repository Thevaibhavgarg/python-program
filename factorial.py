#find a factorial of a given no.
a=int(input("enter a natural no.:"))
fac=1
for i in range (1,a+1):
    fac=fac*i
print("factorial of",a,"is",fac)
