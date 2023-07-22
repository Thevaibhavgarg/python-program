import pickle
data=[]
choice='y'
while( choice=='y' or choice=='Y'):
    roll_no=int(input('Enter the Roll Number of student :'))
    name=input('Enter the name of student :')
    marks=float(input('Enter the marks of student :'))
    record=str(roll_no)+","+name+","+str(marks)+'\n'
    data.append(record)
    choice=input('Press y to enter more record :')
    print(data)
file=open("student1.dat","wb+")
pickle.dump(data,file)
print('Now data of students inserted into file')
file.seek(0) # Now move the file pointer at starting of the file
print('*********A*F*T*E*R*****R*E*A*D*I*N*G********')
print('******F*R*O*M**T*H*E**F*I*L*E**************')
stu_data=pickle.load(file)
for row in stu_data:
          r = row.split(',')  
          rno=r[0]
          name=r[1]
          mark=r[2]
          print('Roll No- ',rno,' Name- ',name,'Marks- ',mark)
file.close()
