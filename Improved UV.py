import numpy as np
import scipy.linalg
import scipy.misc
from matplotlib import pyplot as plt

A = scipy.misc.ascent()  # The matrix representation of the image

k = 50  # Number of basis vectors
m = A.shape[0]  # Choosing the correct dimensions for U
n = A.shape[1]  # Choosing the correct dimensions for V

# The two random matrices
U = np.random.randn(m, k)
V = np.random.randn(n, k)

"""Improving the random basis"""

j = 3  # Number of iterations

for i in range(j):
    U_temp = np.dot(A, V)
    U, R = scipy.linalg.qr(U_temp, mode="economic")
    V_temp = np.dot(A.T, U)
    V, R = scipy.linalg.qr(V_temp, mode="economic")
    
S = np.dot(np.dot(U.T, A), V)
A_UV = np.dot(np.dot(U, S), V.T)

new_A_compressed = A_UV

plt.imshow(new_A_compressed)
plt.title('Improved compression')
plt.show()
"""Clearly a big improvement to the original U and V"""
