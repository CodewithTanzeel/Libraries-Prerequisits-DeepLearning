import numpy as np

# Creating arrays
a = np.array([1, 2, 3])          # 1D array
b = np.array([[1, 2], [3, 4]])    # 2D array

# Array properties
print(a.shape)    # (3,)
print(b.shape)    # (2, 2)
print(a.dtype)    # int64

# Special arrays
zeros = np.zeros((3, 3))      # 3x3 array of zeros
ones = np.ones((2, 2))        # 2x2 array of ones
identity = np.eye(3)          # 3x3 identity matrix
random = np.random.rand(2,3)  # 2x3 random array (0-1)

# Array operations
c = a + 5             # Element-wise addition
d = a * b             # Element-wise multiplication (if shapes match)
e = np.dot(a, b)      # Matrix multiplication
f = np.sum(a)         # Sum of all elements
g = np.mean(a)        # Mean of all elements
h = np.exp(a)         # Exponential function app

# Reshaping and transposing
reshaped = b.reshape(4, 1)
transposed = b.T

# Broadcasting
a = np.array([[1, 2, 3]])
b = np.array([[1], [2], [3]])
c = a + b  # Results in a 3x3 matrix through broadcasting
