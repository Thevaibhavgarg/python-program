print("WELCOME TO VAIBHAV PROGRAM")
file=open("diary.txt","w+")
import datetime
x = datetime.datetime.now()
date=x.strftime("%d %b %Y")
time=x.strftime("%I:%M %p")
file.write(date)
file.write("\n")
file.write(time)
file.write("\n")
name=input("Enter your name:-")
file.write(name)
file.write("\n")
diary=input("start from here:-\n")
file.write(diary)
file.close()

