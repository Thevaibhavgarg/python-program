import pickle
file=open("student1.dat","rb")
stu_data=pickle.load(file)
choice='y'
found=0
while(choice=='y' or choice=='Y'):
    roll=input('Enter the roll no. of student which record you want to display :')
    for row in stu_data:
        r=row.split(',')
        if r[0]==roll:
            print('Search is successful !')
            print('Rolll No. of student :',r[0])
            print('Name of student :',r[1])
            print('Marks of student :',r[2])
            found=1
            break
    if found ==0:
        print('Sorry record is not found of rollno :',roll)
    choice=input('Press y to search data of another student :') 
