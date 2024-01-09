import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class KNN:
    def __init__(self, k=3):
        self.k = k

    def calculate_norm(self, x_train, x_sample):

        distances = (np.sum(((x_train - x_sample[:, np.newaxis, :])**2), axis=2))
        return distances
    
    def predict(self, x_train, y_train, x_sample):
        distances = self.calculate_norm(x_train, x_sample)  # [sample x train_sample]
        sorted_index = np.argsort(distances, axis=1)[:,:self.k] #[sample x train_sample]
        # print(f'{sorted_index.shape=}')
        selected_y=(y_train[sorted_index])
        # print(selected_y.shape)
        y_pred = []

        for each in selected_y:
            y_pred.append(np.argmax(np.bincount(each)))
        return y_pred


if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    model = KNN(k=5)
    predictions = model.predict(X_train, y_train, X_test)
    print(accuracy_score(predictions, y_test))
