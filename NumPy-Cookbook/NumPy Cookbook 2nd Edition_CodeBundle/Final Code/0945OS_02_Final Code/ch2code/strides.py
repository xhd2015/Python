import numpy as np

sudoku = np.array([
   [2, 8, 7, 1, 6, 5, 9, 4, 3],
   [9, 5, 4, 7, 3, 2, 1, 6, 8],
   [6, 1, 3, 8, 4, 9, 7, 5, 2],
   [8, 7, 9, 6, 5, 1, 2, 3, 4],
   [4, 2, 1, 3, 9, 8, 6, 7, 5],
   [3, 6, 5, 4, 2, 7, 8, 9, 1],
   [1, 9, 8, 5, 7, 3, 4, 2, 6],
   [5, 4, 2, 9, 1, 6, 3, 8, 7],
   [7, 3, 6, 2, 8, 4, 5, 1, 9]
   ])

shape = (3, 3, 3, 3)

strides = sudoku.itemsize * np.array([27, 3, 9, 1])

squares = np.lib.stride_tricks.as_strided(sudoku, shape=shape, strides=strides)
print(squares)
