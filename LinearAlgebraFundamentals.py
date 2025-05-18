# Vector operations
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

dot_product = np.dot(v1, v2)  # 1*4 + 2*5 + 3*6 = 32
cross_product = np.cross(v1, v2)  # [-3, 6, -3]

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

matrix_product = A @ B  # Matrix multiplication
determinant = np.linalg.det(A)  # Determinant
inverse = np.linalg.inv(A)  # Matrix inverse
eigenvalues, eigenvectors = np.linalg.eig(A)  # Eigen decomposition

# Solving linear systems
# Ax = b where A=[[1,1],[1,2]], b=[3,5]
A = np.array([[1, 1], [1, 2]])
b = np.array([3, 5])
x = np.linalg.solve(A, b)  # Solution: [1, 2]