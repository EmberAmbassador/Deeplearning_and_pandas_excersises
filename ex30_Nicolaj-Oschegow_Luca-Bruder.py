# Last name(s), first name(s)
import numpy as np
import matplotlib.pyplot as plt


def f(w, b):
    return ((1-w) ** 2) + 100 * ((b - (w ** 2)) ** 2)

def propagate(w, b):
    cost = f(w,b)
    
    #these partial derivatives were calculated by hand. The derivation of these
    #formulas can be found at https://drive.google.com/file/d/1l5GQXET4WLNQ-UQCx6KcMSvBq5OStIPE/view?usp=sharing
    dw = (400 * (w ** 3)) + (2 * w) - (400 * b * w) - 2
    db = (-200 * (w ** 2)) + (200 * b)
    
    gradients = {'dw': dw, 'db': db}
    
    return gradients, cost


def optimize(w, b, num_iter, learning_rate):
    costs = []
    
    for i in range(num_iter):
        try:
            grads, cost = propagate(w,b)
        except OverflowError:
            params = {'w': w, 'b': b}
            print("Overflow occured for learning rate: {}".format(learning_rate))
            return params, grads, costs
            
        
        w = w - learning_rate * grads['dw']
        b = b - learning_rate * grads['db']
        
        costs.append(cost)
    
    params = {'w': w, 'b': b}
    
    return params, grads, costs


# Do not change the following 5 lines - they are needed for the contour plot.
N = 250
lin = np.linspace(-0.2, 1.2, N)
wlin, blin = np.meshgrid(lin, lin)
f_values = f(wlin, blin)
plt.contour(wlin, blin, f_values.reshape(N, N), levels=np.logspace(-1,3,8))

# Find the parameters w and b that minimize f(w,b) and print these parameters as well as the corresponding function value.
w = 0
b = 0
params, grads, costs = optimize(w,b,7500,0.001)
w = params['w']
b = params['b']
print('After 7500 iterations, the optimal values to minimize f(w,b) are: \n' +
      'w: {} \n'.format(w) + 
      'b: {} \n'.format(b))


# Plot (w,b) as a single red point (or red star 'r*').
plt.plot(w,b,'r*')
plt.show()


# Plot the costs
plt.plot(costs)
plt.show()

# e) Perform optimization for different learning rates: 0.001 * i, i = 1,...,9
#   Which learning rates work well, which do not? How can you see this in the 
#   costs plots?

colors = ['Grey','Red','Orange','Yellow','Lime','Green','Cyan','Blue',
          'Purple','Magenta']
w_list = []
b_list = []

fig, axs = plt.subplots(3,3, constrained_layout=True)
for i in range(1,10):
    w = 0
    b = 0
    
    params, grads, costs = optimize(w,b,7500,0.001*i)
    
    w = params['w']
    b = params['b']
    
    w_list.append(w)
    b_list.append(b)
    
    print('Alpha {} : w = {}, b = {}'.format(0.001*i,w,b))
    
    axs[(i-1)//3,(i-1)%3].set_title(round(0.001*i,3))
    axs[(i-1)//3,(i-1)%3].plot(costs, color=colors[i])
    
plt.show()

# Do not change the following 5 lines - they are needed for the contour plot.
N = 250
lin = np.linspace(-0.2, 1.2, N)
wlin, blin = np.meshgrid(lin, lin)
f_values = f(wlin, blin)
plt.contour(wlin, blin, f_values.reshape(N, N), levels=np.logspace(-1,3,8))

plt.xlim(0,1.2)
plt.ylim(0,1.2)
for i in range(0,len(w_list)):
    plt.plot(w_list[i],b_list[i], '*', color=colors[i+1])
plt.show()
    
# The learning rates 0.001 and 0.002 work well. They are the only ones in which
# the cost plots follow a monotonously decreasing function which converges against
# 0. The other learning rates, in comparison, all have a massive increase in 
# cost after a few iterations which far exceed the others 
# (error rate 10-40 in comparison to max error rate 1). These do, however, seem
# to converge again after this initial spike around the 4000th iteration. So
# while they do not perform as well as the initial two, they are still usable
# with high enough iterations. The worst case of all tested learning rates however
# is the learning rate 0.008, which diverges around the 60th iteration so bad
# that it causes an overflow error in the calculation of f, at which point the
# optimization needs to cancel out. Additionally, 0.001 and 0.002 are the only
# ones which reach the local minimum of the contour plot within the allotted 
# 75,000 iterations
    