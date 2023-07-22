#program to find sum of all digit of given no.
a=int(input("enter your no.:"))
res=0
while a>0:
    q=a%10
    res=res+q
    a=a//10
print("sum of all digit of the given no. is:",res)
