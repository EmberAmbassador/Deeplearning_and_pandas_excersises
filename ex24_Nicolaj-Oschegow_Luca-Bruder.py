# Oschegow Nicolaj, Bruder Luca
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)

def plot_min_max(index_min, index_max, array):
    plt.plot(index_min, array[index_min], marker='o', markersize=8, color='green')
    plt.plot(index_max, array[index_max], marker='o', markersize=8, color='red')

# a)

data = np.load('ex24_data.npy')
plt.plot(data)
plt.show()

# b)

min = np.minimum.accumulate(data)

# The maximum profit that can be achieved
maxProfit = 0

# The time of buying and selling to achieve maximum profit
buy = 0
sell = 0

# This calculates the maximum achievable profit as well as the corresponding time
for i in range(len(data)):
    currentProfit = 0
    for j in range(i+1, len(data)):
        currentProfit = data[j] - data[i]
        if currentProfit > maxProfit:
            maxProfit = currentProfit
            buy = i
            sell = j

print("The maximum profit that can be achieved with one transaction is: " + str(maxProfit)) 

# c)

print("To achieve maximum profit you should buy at " + str(buy) + " and sell at " + str(sell))

plot_min_max(buy, sell, data)
plt.plot(data)
plt.show()

# d)

randArray = np.random.randint(0,101,50)
for i in range(1, len(randArray) - 1):
    if randArray[i-1] < randArray[i] < randArray[i+1]:
        print(str(randArray[i]))
