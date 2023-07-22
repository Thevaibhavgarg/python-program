# THIS IS A PROGRAM OF CALCULATOR
print('+ stand for additon\n- stand for subtraction\n* stand for multipication\n/ stand for division\n** stand for power')
n=int(input('ENTER HOW MANY TIMES YOU WANT TO CALCUTATE:'))
for i in range (n):
 q=input('ENTER YOUR OPRESATION:')
 if q=='+':
     w=int(input('ENTER YOUR FIRST NO.:'))
     e=int(input('ENTER YOUR FIRST NO.:'))
     r=w+e
     print('YOUR ANSWER IS',r)
     print("*"*20)
 elif q=='-':
     t=int(input('ENTER YOUR FIRST NO.:'))
     y=int(input('ENTER YOUR FIRST NO.:'))
     u=t-y
     print('YOUR ANSWER IS',u)
     print("*"*20)
 elif q=='*':
     i=int(input('ENTER YOUR FIRST NO.:'))
     o=int(input('ENTER YOUR FIRST NO.:'))
     p=i*o
     print('YOUR ANSWER IS',p)
     print("*"*20)
 elif q=='/':
     a=int(input('ENTER YOUR FIRST NO.:'))
     s=int(input('ENTER YOUR FIRST NO.:'))
     d=a/s
     print('YOUR ANSWER IS',d)
     print("*"*20)
 elif q=='**':
     f=int(input('ENTER YOUR FIRST NO.:'))
     g=int(input('ENTER YOUR FIRST NO.:'))
     h=f**g
     print('YOUR ANSWER IS',h)
     print("*"*20)
    
    
        
