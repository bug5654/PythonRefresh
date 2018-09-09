import numpy as np

a = np.arange(15).reshape(3, 5)
print("a: " + str(a))
print("a.shape(): " + str(a.shape))
print("a.ndim(): " + str(a.ndim))
print("a.itemsize(): " + str(a.itemsize))
print("a.size(): " + str(a.size))
print("type(a): " + str(type(a)))
b = np.array([6,7,8])
print("b: " + str(b))
print("type(b): " + str(type(b)))