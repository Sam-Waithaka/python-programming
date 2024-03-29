import numpy as np

a = np.zeros(10)
print(a)

b = np.full((2,10), 0.7)
print(b)

c = np.linspace(0,25,7)
print(c)

print(type(c))

'''
The zeros() function inside numpy creates an array with n number of zeroes inside it.

The full() function creates a two-dimensional matrix of dimensions 2 x 10 consisting only of the values 0.7.

linspace() function divides the values between 0 and 25 in 7 equal parts. The resultant matrix is in the output.

when you see the data type of c, it is a special data-type created and used in numpy called as ndarray. 
If you try the output for a and b, it will also be ndarray as numpy deals exclusively with ndarray, which is a substitute for lists and is far more efficient. 
'''