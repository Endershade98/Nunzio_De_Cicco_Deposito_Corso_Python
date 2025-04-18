import numpy as np
import random



x = np.array([1, 0, 3, -5])
print(x**2)
print(x-2)

y = np.array([[1, 0, -1],[0, 2, -3]])
print(y)

z = np.array([c for c in range(9)])
print(z)
z.reshape(3,3)
print(z)

v = np.linspace(0, 10)
w = np.random(0, 10)
print(v)
print(w)