## Here, we applied PCA from scratch by using Numpy

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components

    def fit(self, X):
        self.mean = np.mean(X, axis=0)
        X = X - self.mean
        cov = np.cov(X.T)
        _, eigenvectors = np.linalg.eig(cov)
        self.eigenvectors = eigenvectors[:, :self.n_components]

    def transform(self, X):
        X = X - self.mean
        return np.dot(X, self.eigenvectors)

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
    
    def inverse_transform(self, X):
        return np.dot(X, self.eigenvectors.T) + self.mean
    
if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    model = PCA(n_components=2)
 
    # visualize the data after applying PCA
    X_train = model.fit_transform(X_train)
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
    plt.show()