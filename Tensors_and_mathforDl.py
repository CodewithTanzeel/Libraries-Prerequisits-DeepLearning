# numpy_dl.py
import numpy as np

def numpy_basics():
    # 1D and 2D arrays (tensors)
    a = np.array([1, 2, 3])          # Vector
    b = np.array([[1, 2], [3, 4]])   # Matrix
    print("Vector:\n", a)
    print("Matrix:\n", b)

def dl_operations():
    # Matrix multiplication (used in dense layers)
    W = np.random.rand(3, 2)  # Weight matrix (3x2)
    X = np.random.rand(2, 1)  # Input (2x1)
    output = np.dot(W, X)     # Forward pass (3x1)
    print("Matrix multiplication (W @ X):\n", output)

    # ReLU activation
    Z = np.array([[-1, 2], [0.5, -3]])
    relu = np.maximum(0, Z)
    print("ReLU output:\n", relu)

if __name__ == "__main__":
    print("=== NumPy for Deep Learning ===")
    numpy_basics()
    dl_operations()