import numpy as np

A = np.array([[2, 3],
               [1, -1]])
B = np.array([7, 1])

solusi1 = np.linalg.solve(A1, b1)
print("Solusi untuk soal 1:")
print(f"x = {solusi1[0]}, y = {solusi1[1]}")
