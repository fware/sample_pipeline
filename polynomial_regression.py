# Importing libraries

import numpy as np

import math

import matplotlib.pyplot as plt


# Univariate Polynomial Regression

class PolynomailRegression():

    def __init__(self, degree, learning_rate, iterations):
        self.w = None
        self.n = None
        self.m = None
        self.y_data = None
        self.x_data = None
        self.degree = degree
        self.learning_rate = learning_rate
        self.iterations = iterations

    # function to transform X
    def transform(self, x_data):

        # initialize x_transform
        x_transform = np.ones((self.m, 1))
        j = 0

        for j in range(self.degree + 1):

            if j != 0:
                x_pow = np.power(x_data, j)
                # append x_pow to x_transform
                x_transform = np.append(x_transform, x_pow.reshape(-1, 1), axis=1)

        return x_transform

    # function to normalize X_transform
    def normalize(self, x):
        x[:, 1:] = (x[:, 1:] - np.mean(x[:, 1:], axis=0)) / np.std(x[:, 1:], axis=0)
        return x

    # model training
    def fit(self, x, y):
        self.x_data = x
        self.y_data = y
        self.m, self.n = self.x_data.shape

        # weight initialization
        self.w = np.zeros(self.degree + 1)

        # transform X for polynomial h( x ) = w0 * x^0 + w1 * x^1 + w2 * x^2 + ........+ wn * x^n
        x_transform = self.transform(self.x_data)

        # normalize x_transform
        x_normalize = self.normalize(x_transform)

        # gradient descent learning
        for i in range(self.iterations):
            h = self.predict(self.x_data)
            error = h - self.y_data

            # update weights
            self.w = self.w - self.learning_rate * (1 / self.m) * np.dot(x_normalize.T, error)

        return self

    # predict
    def predict(self, x_data):
        # transform X for polynomial h( x ) = w0 * x^0 + w1 * x^1 + w2 * x^2 + ........+ wn * x^n
        x_transform = self.transform(x_data)
        x_normalize = self.normalize(x_transform)
        return np.dot(x_transform, self.w)


# Driver code

def main():
    # Create dataset
    independent_x = np.array([[1], [2], [3], [4], [5], [6], [7]])
    dependent_y = np.array([45000, 50000, 60000, 80000, 110000, 150000, 200000])

    # model training
    model = PolynomailRegression(degree=2, learning_rate=0.01, iterations=500)
    model.fit(independent_x, dependent_y)

    # Prediction on training set
    y_pred = model.predict(independent_x)

    # Visualization
    plt.scatter(independent_x, dependent_y, color='blue')
    plt.plot(independent_x, y_pred, color='orange')
    plt.title('X vs Y')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


if __name__ == "__main__":
    main()
