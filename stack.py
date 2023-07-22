#stack
def push(list,ele):
	list.append(ele)
	print(list)
def pop(list):
	rem=list.pop()
	print(rem,"remove form the list")
	print(list)
#main
a=[]
print("entered list is",a)
choice=input("enter y if you want to add element:")
while choice=="y" or choice=="Y":
   b=input("enter element you want to add:")
   push(a,b)
   choice=input("enter y if you want to add element:")
print("*"*30)
choice2=input("enter y if you want to remove element:")
while choice2=="y" or choice2=="Y":
	pop(a)
	choice2=input("enter y if you want to add element:")
	