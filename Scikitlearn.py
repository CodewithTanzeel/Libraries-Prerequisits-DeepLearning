
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def preprocess_and_visualize():
    # Load Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Standardize features (critical for DL)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Dimensionality reduction (like an autoencoder)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    # Plot PCA results (latent space)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.title("PCA of Iris Dataset (2D Projection)")
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    print("=== Scikit-learn for Deep Learning ===")
    preprocess_and_visualize()
