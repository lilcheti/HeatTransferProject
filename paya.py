# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix

from math import pi, sin

def seidel(a, x ,b):
	#Finding length of a(3)	
	n = len(a)				
	# for loop for 3 times as to calculate x, y , z
	for j in range(0, n):		
		# temp variable d to store b[j]
		d = b[j]				
		
		# to calculate respective xi, yi, zi
		for i in range(0, n):	
			if(j != i):
				d-=a[j][i] * x[i]
		# updating the value of our solution		
		x[j] = d / a[j][j]
	# returning our updated solution		
	return x

#constants
n = 1
q = 100
T0 = 100
Tinf = 500
hinf = 100
k = 100
# plane diameters
Nx = 6
L = 100
Ny = 5
W = 200
deltax = L/Nx
deltay = W/Ny
#first line has T
Ny = Ny - 1
# aT = b						
a = []							
b = []		
# initial solution depending on n(here n=3)					
T = []						
A = []
B = []
a = []
for i in range(0,(Nx*Ny)):
    T.append(0)
    a.append(0)

#first lane 
Tfirst = []
for i in range(0,Nx):
    Tfirst.append(T0*(1+sin((pi*i*deltax)/(n*L))))
print("first lane:",Tfirst)

#left corner up
a[0] = deltax/deltay+deltay/deltax
a[1] = -deltay/deltax
a[6] = -deltax/(2*deltay)
A.append(a)
B.append((q*deltay/k)+(deltax*Tfirst[0]/(2*deltay)))

a = []
for i in range(0,(Nx*Ny)):
    a.append(0)

#right corner up
a[Nx-1] = deltax/deltay+deltay/deltax+hinf*deltay
a[Nx-1+Nx] = -deltax/(2*deltay)
a[Nx-2] = -deltay/deltax
A.append(a)
B.append((hinf*deltay*Tinf/k)+(deltax*Tfirst[Nx-1]/(2*deltay)))

a = []
for i in range(0,(Nx*Ny)):
    a.append(0)


print(A,B)

#loop run for m times depending on m the error value
for i in range(0, 25):			
	T = seidel(A, T, B)
	#print each time the updated solution
	print(T)					
