## K-Means implementation with NumPy from scratch

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

class KMeans:
    def __init__(self, k=3, max_iter=100):
        self.k = k
        self.max_iter = max_iter

    def fit(self, X):
        self.X = X
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]

        for _ in range(self.max_iter):
            distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
            labels = np.argmin(distances, axis=1)

            new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])

            if np.allclose(self.centroids, new_centroids):
                break

            self.centroids = new_centroids

    def predict(self):
        distances = np.linalg.norm(self.X[:, np.newaxis] - self.centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        return labels

    def score(self, y):
        y_pred = self.predict()
        return np.sum(y_pred == y) / len(y)
    

if __name__ == '__main__':

    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    # Create an instance of KMeans with k=3
    kmeans = KMeans(k=3)
    # Fit the KMeans model to the data
    kmeans.fit(X)
    # Predict the cluster labels for the data points
    labels = kmeans.predict()

    # Visualize the clusters
    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='red', marker='x')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('KMeans Clustering')
    plt.show()