a=int(input("enter your no.:"))
b=a
rem=0
rev=0
while(b>0):
    rem=b%10
    rev=rev*10+rem
    b=b//10
if a==rev: 
    print(a,"it is a palindrome")
else:
    print(a,"it is not a palindrome")
