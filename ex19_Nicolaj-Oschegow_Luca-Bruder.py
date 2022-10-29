# Oschegow Nicolaj, Bruder Luca

import math
import numpy as np

np.random.seed(0)

# a)

#X = np.array([[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]])

X = np.arange(16)

X_sqrt = np.array([])

# Calculate the squareroot for each element of X and write it into X_sqrt
for element in X:
    root = math.sqrt(element)
    X_sqrt = np.append(X_sqrt, [root])

X_2 = np.array([])

# Calculate the square for each element of X and write it into X_2
for element in X:
    sqr = element**2
    X_2 = np.append(X_2, [sqr])


# Stack the arrays X_sqrt and X_2 to create a new 2 dimensional array
XX = np.hstack(([X_sqrt], [X_2]))


# An attempt to get XX in the desired shape. It does not work.
#XX = np.array([])
#for i in range(16):
#    XX = np.append(XX, np.hstack([[X_2[i], X_sqrt[i]]]))

print(XX)



# b)

# Create an array of size 1000 x 5 of random numbers from the normal distribution with variance a^2 and mean b
a = 5
b = 4
M = math.sqrt(a) * np.random.randn(1000, 5) + b


# c)
# i)
# Create a new file for part i
f = open("i_normal_distribution.npy", "w")
f.close()

np.save('i_normal_distribution', M)
M_i = np.load('i_normal_distribution.npy')

# ii)

np.savetxt('ii_normal_distribution', M)
M_ii = np.loadtxt('ii_normal_distribution')

# The created textfile (ii_normal_distribution) is about three times bigger than the created npy file (i_normal_distribution).


# d)

for j in range(5):
    print("Column " + str(j) + ":")
    print("The mean is: " + str(M.mean(0)[j]) + " compared to: " + str(b))
    print("The variance is: " + str(np.var(M, 0)[j]) + " compared to: " + str(a))
    print("The maximum is: " + str(M.max(0)[j]) + " and the minimum is: " + str(M.min(0)[j]))
    print("---------------------------------------")


# e)

M = np.delete(M, 2, 0)


# f)

M3 = np.array([])

# Write all negative numbers found in M into M3
for col in M:
    for element in col:
        if element < 0:
            M3 = np.append(M3, [element])

# Replace each positive number in M with 0
M = np.where(M>=0, 0, M)











