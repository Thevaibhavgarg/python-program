"""
n=int(input())
g=0
t=0
h=(2*n)-1
for i in range(n):
	for j in range(n):
		if(j>=i):
			print(n-g,end=" ")
		else:
			print(n-j,end=" ")
	g=g+1
	print()
"""

"""
n=int(input())
g=0
t=0
h=(2*n)-1
for i in range(n,1,-1):
	for j in range(n,1,-1):
		if(j<=i):
			print(n-g,end=" ")
		else:
			print(n-j,end=" ")
	g=g-1
	print()
"""
n=int(input())
h=(2*n-1)
r=0
q=0
w=0
v=0
a=1
e=0
for i in range(h):
	if i<n:
		for j in range(h):
					if(i==0 or j==0 ):
						print(n,end=" ")
					elif( j<=r):
						print(n-1-q,end=" ")
						q=q+1
					elif(j>r and j<h-1-r):
						print(n-v,end=" ")
					elif( j>=h-1-r and j<h):
						if(i==n-1 and j>=n):
							print(n-v+w+1,end=" ")
							w=w+1
						else:
							print(n-v+w,end=" ")
							w=w+1
					else:
						print(" ",end=" ")
		print()
		r=r+1
		v=v+1
		q=0
		w=0
		
	else:
		f=i
		g=i-r+2
		
		for j in range(h):
			if(i==h-1 or j==0  ):
				print(n,end=" ")
			elif( j<f-a):
				print(n-1-q,end=" ")
				q=q+1
			elif(j>=f-a and j<h-1-w-r+2):
				print(g,end=" ")
			elif(j>=h-1-w-r+2 and j<h):
				print(g+e,end=" ")
				e=e+1
			else:
				print(" ",end=" ")
		print()
		f=f+1
		e=0
		q=0
		w=w-1
		g=g+1
		a=a+2

