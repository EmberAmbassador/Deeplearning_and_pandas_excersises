# Exercise 2
# a) In python 'inf' represents infinity. It occurs for example as
#    the result of float('Inf') or math.inf.
#    It can for example be used to check wether some float
#    variable x is infinitely big. float('Inf') <= x

# b) Boolean variables can either be true or false. In python
#    these values have to be capitalised (True and False).

# c)
import numpy as np
epsilon = np.finfo(float).eps

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
if abs(x - y) <= max(abs(x), abs(y)) * epsilon:
    print("The two numbers are identical.")
else:
    print("The two numbers are different.")

#    The presented code would be a bad idea since we are
#    comparing floats. These often get rounded in a way which
#    leads to false results.
#    An example of this would be the following:

#origin = 10.0
#temp = origin / 77
#end = temp * 77
#if origin == end:
#    print("The are identical")
#else:
#    print("The numbers seem to be different") 

#    Even though origin and end should have the exact same
#    value, they do not. 
#    
#    The solution we therefor implemented has a certain error
#    range (epsilon) and checks whether the difference between
#    the two values is bigger than our tolerance or not.
