# visualization_dl.py
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits

def plot_loss():
    # Simulate training loss
    epochs = range(1, 6)
    loss = [0.5, 0.3, 0.2, 0.1, 0.05]
    plt.plot(epochs, loss, marker='o')
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.title("Training Loss Over Epochs")
    plt.grid()
    plt.show()

def plot_images():
    # Load MNIST-like digits
    digits = load_digits()
    plt.figure(figsize=(10, 4))
    for i in range(5):
        plt.subplot(1, 5, i+1)
        plt.imshow(digits.images[i], cmap='gray')
        plt.axis('off')
    plt.suptitle("MNIST Digit Samples")
    plt.show()

if __name__ == "__main__":
    print("=== Visualization for Deep Learning ===")
    plot_loss()
    plot_images()