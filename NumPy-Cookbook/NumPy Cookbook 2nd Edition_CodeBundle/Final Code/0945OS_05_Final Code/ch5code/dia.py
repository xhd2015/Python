import numpy as np 
import scipy.sparse as sps 
import matplotlib.pyplot as plt

data = np.array([[1, 2, 3, 4]]).repeat(3, axis=0)
offsets = np.array([0, -1, 2]) 
mtx = sps.dia_matrix((data, offsets), shape=(4, 4)) 
print mtx
