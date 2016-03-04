import numpy as np

x = np.array([[1, 2], [3, 4]])
y = memoryview(x)
print(y.format)
print(y.itemsize)
print(y.ndim)
print(y.readonly)
print(y.shape)
print(y.strides)

z = np.asarray(y)
print(z)
x[0,0] = 9
print(z)
