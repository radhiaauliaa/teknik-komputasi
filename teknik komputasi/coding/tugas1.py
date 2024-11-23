"""
Nama   : Radhia Aulia Nisa
Nim    : 23343049
Prodi  : Informatika
Matkul : Teknik Komputasi
"""

import numpy as np

# Matriks koefisien dan vektor konstanta
A = np.array([[1, 1, 1], [1, 2, -1], [2, 1, 2]], dtype=float)
B = np.array([6, 2, 10], dtype=float)

# Eliminasi Gauss
for i in range(2):
    for j in range(i+1, 3):
        factor = A[j, i] / A[i, i]
        A[j] -= factor * A[i]
        B[j] -= factor * B[i]

# Substitusi mundur
X = np.zeros(3)
for i in range(2, -1, -1):
    X[i] = (B[i] - np.dot(A[i, i+1:], X[i+1:])) / A[i, i]

# Hasil akhir
print(f"x1 = {X[0]}\nx2 = {X[1]}\nx3 = {X[2]}")
