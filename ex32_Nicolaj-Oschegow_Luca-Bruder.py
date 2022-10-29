# Oschegow Nicolaj, Bruder Luca
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

df = pd.read_csv("ex32_data.csv")
np.random.seed(0)

# a)

y = df['Outcome']
print(y.shape)
x = df.loc[:,'Pregnancies':'Age']
print(x.shape)

allIndices = np.arange(768)
testIndices = np.random.choice(768, 192, replace=False)
trainIndices = np.setdiff1d(allIndices, testIndices)

train_set_x = x.loc[trainIndices].to_numpy().T
train_set_y = y.loc[trainIndices].to_numpy().T

test_set_x = x.loc[testIndices].to_numpy().T
test_set_y = y.loc[testIndices].to_numpy().T

test_set_y = test_set_y.reshape(1, -1)
train_set_y = train_set_y.reshape(1, -1)


# b)

def initialize_parameters(dim):
    w = np.random.randn(dim, 1)
    b = 0.
    return w, b

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def propagate(w, b, X, y):
    m = X.shape[1]
    # Calculate a
    z = np.dot(w.T, X) + b
    a = sigmoid(z)
    cost = - 1/m * np.sum(y * np.log(a) + (1-y) * np.log(1-a))
    # Calculate dw, db
    dw = 1/m * np.dot(X, (a - y).T)
    db = 1/m * np.sum(a - y)
    cost = np.squeeze(cost)

    # Check if cost is NaN and if so change it
    if cost == float('nan'):
        cost = np.inf

    grads = {'dw': dw,
    'db': db}
    return grads, cost

def optimize(w, b, X, y, num_iter, learning_rate):
    costs = []
    for i in range(num_iter):
        grads, cost = propagate(w, b, X, y)
        w = w - learning_rate * grads['dw']
        b = b - learning_rate * grads['db']
        if i % 10000 == 0:
            costs.append(cost)
            # Output the quadratic Euclidean norm of the gradient of the cost
            print(np.sum(grads['dw'] ** 2)+ np.sum(grads['db'] ** 2))
    params = {'w': w,'b': b}
    return params, grads, costs

def predict(w, b, X):
    a = sigmoid(np.dot(w.T, X) + b)
    a[a>=0.5] = 1.
    a[a<0.5] = 0.
    return a

def model(x_train, y_train, x_test, y_test, num_iter, learning_rate):
    n = x_train.shape[0]
    w, b = initialize_parameters(n)
    params, grads, costs = optimize(w, b, x_train, y_train, num_iter,learning_rate)
    y_hat_train = predict(params['w'], params['b'], x_train)
    y_hat_test = predict(params['w'], params['b'], x_test)
    print('training error: ', np.mean(np.abs(y_hat_train - y_train)))
    print('test error: ', np.mean(np.abs(y_hat_test- y_test)))
    return params, costs



# c)

#print(train_set_x[1,:].reshape(1, -1).shape)
#print(train_set_y.shape)

print(train_set_x.shape)
print(train_set_y.shape)

#params, costs = model(train_set_x[1,:].reshape(1, -1), train_set_y, test_set_x[1,:].reshape(1, -1),test_set_y, 1000001, 0.00025)
params, costs = model(train_set_x, train_set_y, test_set_x,test_set_y, 1000001, 0.00025)

plt.plot(costs)
plt.show()


# d)

predictions = predict(params['w'], params['b'], test_set_x)


cnf_matrix = metrics.confusion_matrix(test_set_y.flatten(), predictions.flatten())

print(cnf_matrix)


# e)

# Learning rate: 0.00025, steps: 100001
params, costs = model(train_set_x, train_set_y, test_set_x,test_set_y, 100001, 0.00025)
predictions = predict(params['w'], params['b'], test_set_x)
cnf_matrix = metrics.confusion_matrix(test_set_y.flatten(), predictions.flatten())
print(cnf_matrix)

# Learning rate: 0.00025, steps: 10001
params, costs = model(train_set_x, train_set_y, test_set_x,test_set_y, 10001, 0.00025)
predictions = predict(params['w'], params['b'], test_set_x)
cnf_matrix = metrics.confusion_matrix(test_set_y.flatten(), predictions.flatten())
print(cnf_matrix)


# Learning rate: 0.0002, steps: 1000001
params, costs = model(train_set_x, train_set_y, test_set_x,test_set_y, 1000001, 0.0002)
predictions = predict(params['w'], params['b'], test_set_x)
cnf_matrix = metrics.confusion_matrix(test_set_y.flatten(), predictions.flatten())
print(cnf_matrix)

# Learning rate: 0.0002, steps: 100001
params, costs = model(train_set_x, train_set_y, test_set_x,test_set_y, 100001, 0.0002)
predictions = predict(params['w'], params['b'], test_set_x)
cnf_matrix = metrics.confusion_matrix(test_set_y.flatten(), predictions.flatten())
print(cnf_matrix)