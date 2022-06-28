# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix

from math import pi, sin

def seidel(a, x ,b):
	#Finding length of a(3)	
	n = len(a)				
	print(n)
	# for loop for 3 times as to calculate x, y , z
	for j in range(0, n):		
		# temp variable d to store b[j]
		d = b[j]				
		
		# to calculate respective xi, yi, zi
		for i in range(0, n):	
			if(j != i):
				d-=a[j][i] * x[i]
		# updating the value of our solution	
		if a[j][j] != 0:	
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
    T.append(100)
    a.append(0)

#first lane 
Tfirst = []
for i in range(0,Nx):
    Tfirst.append(T0*(1+sin((pi*i*deltax)/(n*L))))
print("first lane:",Tfirst)

#left corner up
a[0] = deltax/deltay+deltay/deltax
a[1] = -deltay/deltax
a[Nx] = -deltax/(2*deltay)
A.append(a)
B.append((q*deltay/k)+((deltax*Tfirst[0])/(2*deltay)))

a = []
for i in range(0,(Nx*Ny)):
    a.append(0)

#right corner up
a[Nx-1] = deltax/deltay+deltay/deltax+hinf*deltay/k
a[Nx-1+Nx] = -deltax/(2*deltay)
a[Nx-2] = -deltay/deltax
A.append(a)
B.append((hinf*deltay*Tinf/k)+(deltax*Tfirst[Nx-1]/(2*deltay)))

a = []
for i in range(0,(Nx*Ny)):
    a.append(0)
#left corner bottom
a[(Ny-1)*Nx] = (deltax/(2*deltay))+(deltay/(2*deltax))
a[(Ny-2)*Nx] = -deltax/(2*deltay)
a[1+Nx*(Ny-1)] = -deltay/(2*deltax)
A.append(a)
B.append(q*deltay/(2*k))

a = []
for i in range(0,(Nx*Ny)):
    a.append(0)
	
#right corner bottom
a[Nx-1+Nx*(Ny-1)] = deltax/(2*deltay)+deltay/(2*deltax)+hinf*deltay/(2*k)
a[Nx-1+Nx*(Ny-2)] = -deltax/(2*deltay)
a[Nx-2+Nx*(Ny-1)] = -deltay/(2*deltax)
A.append(a)
B.append(hinf*deltay*Tinf/(2*k))



#right lane
for j in range(1,Ny-1):
	a = []
	for i in range(0,(Nx*Ny)):
		a.append(0)
	a[Nx-1+j*Nx] = deltax/deltay+deltay/deltax+hinf*deltay/k
	a[Nx-1+Nx*(j-1)] = -deltax/(2*deltay)
	a[Nx-1+Nx*(j+1)] = -deltax/(2*deltay)
	A.append(a)
	B.append(hinf*deltay*Tinf/k)

#left lane
for j in range(1,Ny-1):
	a = []
	for i in range(0,(Nx*Ny)):
		a.append(0)
	a[Nx*j] = deltax/deltay + deltay/deltax
	a[1+j*Nx] = -deltay/deltax
	a[Nx*(j-1)] = -deltax/(2*deltay)
	a[Nx*(j+1)] = -deltax/(2*deltay)
	A.append(a)
	B.append(q*deltay/k)
#top lane
for i in range(1,Nx-1):
	a = []
	for k in range(0,(Nx*Ny)):
		a.append(0)
	a[i] = 2*deltax/deltay+2*deltay/deltax
	a[i+1] = -deltay/deltax
	a[i+Nx] = -deltax/deltay
	a[i-1] = -deltay/deltax
	A.append(a)
	B.append(deltax*Tfirst[i]/deltay)
#bottom lane
for i in range(1,Nx-1):
	a = []
	for k in range(0,(Nx*Ny)):
		a.append(0)
	a[i+Nx*(Ny-1)] = deltax/deltay + deltay/deltax
	a[i+Nx*(Ny-2)] = -deltax/deltay
	a[i+1+Nx*(Ny-1)] = -deltay/(2*deltax)
	a[i-1+(Nx*(Ny-1))] = -deltay/(2*deltax)
	A.append(a)
	B.append(0)
#inside
for i in range(1,Nx-1):
	for j in range(1,Ny-1):
		a = []
		for k in range(0,(Nx*Ny)):
			a.append(0)
		a[i+j*Nx] = 2*deltax/deltay+2*deltay/deltax
		a[i+(j-1)*Nx] = -deltax/deltay
		a[i+1+j*Nx] = -deltay/deltax
		a[i+(j+1)*Nx] = -deltax/deltay
		a[i-1+j*Nx] = -deltay/deltax
		A.append(a)
		B.append(0)

print(A,B)

#loop run for m times depending on m the error value
for i in range(0, 25):			
	T = seidel(A, T, B)
	#print each time the updated solution
	print(T)					
