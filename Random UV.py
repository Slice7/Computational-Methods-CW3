import numpy as np
import scipy.misc
from matplotlib import pyplot as plt

A = scipy.misc.ascent()  # The matrix representation of the image

plt.imshow(A)
plt.title('Original image')
plt.show()
"""The original image"""

k = 50  # Number of basis vectors
m = A.shape[0]  # Choosing the correct dimensions for U
n = A.shape[1]  # Choosing the correct dimensions for V

# The two random matrices
U = np.random.randn(m, k)
V = np.random.randn(n, k)

S = np.dot(np.dot(U.T, A), V)
A_UV = np.dot(np.dot(U, S), V.T)  # Projecting the picture onto the random matrices

A_compressed = A_UV

plt.imshow(A_compressed, cmap=plt.gray())
plt.title('Random compression')
plt.show()
"""We can see that using random U and V yields a very inaccurate projection of A"""
