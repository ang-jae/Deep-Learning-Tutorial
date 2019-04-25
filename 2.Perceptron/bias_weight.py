import numpy as np
x = np.array([0, 1]) #input
w = np.array([0.5, 0.5]) #weight
b = -0.7 #bias
print(w*x)
print(np.sum(w*x))
print(np.sum(w*x) + b)