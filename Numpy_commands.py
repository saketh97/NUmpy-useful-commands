import numpy as np
import matplotlib.pyplot as plt

#random library

np.random.rand(3,2) #create a 3x2 array of random values between 0 and 1

np.random.randn(3,3) #creates a random 3x3 array of values from standard normal distribution

np.random.randint(1,5,size=(2,2)) #create array of size 10 with values between 1(inclusive) to 5(exclusive)

np.random.random() #returns a random sample between 0.0(exclusive) and 1.0(inclusive)
np.random.sample() #returns a random sample between 0.0(exclusive) and 1.0(inclusive)

df = np.array([22,34,56])
np.random.choice(df,1,p=[0.1,0.6,0.3])  #choose 1 number from df where p is probabilites of there occurences

np.random.choice(4,3,replace = True) #choose 3 number between 0-4(exclusive) where repition is allowed
np.random.choice(4,3,replace = False) #choose 3 number between 0-4(exclusive) where repition is not allowed


n, p = 10, 0.5  # number of trials, probability of each trial
s = np.random.binomial(n, p, 1000)
# result of flipping a coin 10 times, tested 1000 times.
plt.hist(s)

mean, std = 2, 0.1 # mean and standard deviation
s = np.random.normal(mean, std, 1000)
plt.hist(s)#binomial distribution is discrete and normal idstribution is continous.

s = np.random.uniform(-1,0,1000)
plt.hist(s)#uniform distribution of between -1 and 0 form 1000 times

np.random.permutation(10) #randomly arrange array of numbers between 0-9.

np.random.permutation([1, 4, 9, 12, 15]) #random arrange the mentioned numbers in that array.


#linear algebra library

np.dot(3,5) #dot product of two values

a = np.array([1,2],[3,4])
b = np.array([4,5],[6,7])
np.dot(a,b) #returns dot product of two matrices

np.dot([2j, 3j], [2j, 3j]) #dotproduct of conjugates


a = np.array([1,2],[3,4])
b = np.array([4,5],[6,7])
c=np.array([[2,3],[3,4]])    #the dot product of two or more arrays in a single function call,
np.linalg.multi_dot([a,b,c]) #while automatically selecting the fastest evaluation order.

a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
np.matmul(a, b)   #matrix multiplication of two arrays.

b = [[4, 1], [2, 2]]
np.linalg.matrix_power(b,2) #Raise a square matrix to the (integer) power 2.

A = np.array([[1,-2j],[2j,5]])
L = np.linalg.cholesky(A) #Cholesky decomposition of a matrix.

np.linalg.eigvals(a) #returns eigen values of matrix 'a'
a = np.array([[1,2,3],[4,5,6],[7,8,9]])


a = np.array([[1,2,3],[4,5,6],[7,8,9]])
w,v = np.linalg.eig(a)   # computes eigen values and right eigen vectors of square array
