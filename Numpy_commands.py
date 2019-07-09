import numpy as np

#basic commands
array_1d = np.array([10,22,53,14,75])     #to create a 1D array using numpy
print(array_1d)

len(array_1d)    #display length of array

array_1d.sum()   #display sum of elements in array

array_1d.max()  #display mamimum value element in array

array_1d.min() #display minimum value element in array

#random library

np.random.rand(3,2) #create a 3x2 array of random values between 0 and 1

np.random.randn(3,3) #creates a trandom 3x3 array of values

np.random.randint(5,size=10) #create array of size 10 with values between 0-5(exclusive)

 np.random.random_sample() #returns a random sample between 0.0(exclusive) and 1.0
