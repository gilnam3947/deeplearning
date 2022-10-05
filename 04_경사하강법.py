#경사하강법

#!pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

plt.scatter(x, y)
plt.show()

a = 0
b = 0

lr = 0.03

epochs = 2001

n = len(x)

#경사하강법
for i in range(epochs):
    y_pred = a * x + b
    error = y - y_pred
    
    a_diff = (2/n) * sum(-x * (error))
    b_diff = (2/n) * sum(-(error))
    
    a = a - lr * a_diff
    b = b - lr * b_diff
    
    if i % 100 == 0:
        print("epochs=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))
        
    y_pred = a * x + b
    
plt.scatter(x, y)
plt.plot(x, y_pred, 'r')
plt.show()
