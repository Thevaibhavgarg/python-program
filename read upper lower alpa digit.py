digit=0
alpha=0
lower=0
upper=0
file=open("mob.txt","r")
q=file.read()
for i in q:
	if i.isupper():
		upper+=1
	if i.islower():
		lower+=1
	if i.isdigit():
		digit+=1
	if i.isalpha():
		alpha+=1
print("digit:",digit)
print("alpha:",alpha)
print("lower:",lower)
print("upper:",upper)