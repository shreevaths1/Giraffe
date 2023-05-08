import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(type(a))

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 2], [2, 2]])
Z = np.dot(X, Y)
print(Z)
