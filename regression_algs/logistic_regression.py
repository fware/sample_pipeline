# Importing libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings("ignore")

# to compare our model's accuracy with sklearn model
from sklearn.linear_model import LogisticRegression


# Logistic Regression
class LogitRegression():
    def __init__(self, learning_rate, iterations):
        self.learning_rate = learning_rate
        self.iterations = iterations

    # Function for model training
    def fit(self, x, y):
        # no_of_training_examples, no_of_features
        self.m, self.n = x.shape
        # weight initialization
        self.w = np.zeros(self.n)
        self.b = 0
        self.x = x
        self.y = y

        # gradient descent learning

        for i in range(self.iterations):
            self.update_weights()
        return self

    # Helper function to update weights in gradient descent
    def update_weights(self):
        A = 1 / (1 + np.exp(- (self.x.dot(self.w) + self.b)))

        # calculate gradients
        tmp = (A - self.y.T)
        tmp = np.reshape(tmp, self.m)
        dW = np.dot(self.x.T, tmp) / self.m
        db = np.sum(tmp) / self.m

        # update weights
        self.w = self.w - self.learning_rate * dW
        self.b = self.b - self.learning_rate * db

        return self

    # Hypothetical function h( x )

    def predict(self, x):
        Z = 1 / (1 + np.exp(- (x.dot(self.w) + self.b)))
        y = np.where(Z > 0.5, 1, 0)
        return y

    # Driver code


def main():
    # Importing dataset
    df = pd.read_csv("diabetes.csv")
    x = df.iloc[:, :-1].values
    y = df.iloc[:, -1:].values

    # Splitting dataset into train and test set
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=1 / 3, random_state=0)

    # Model training
    model = LogitRegression(learning_rate=0.01, iterations=900)  # From the local class
    model.fit(x_train, y_train)

    model1 = LogisticRegression()   # From sklearn.linear_model
    model1.fit(x_train, y_train)

    # Prediction on test set
    y_pred = model.predict(x_test)
    y_pred1 = model1.predict(x_test)

    # measure performance
    correctly_classified = 0
    correctly_classified1 = 0

    # counter
    count = 0
    for count in range(np.size(y_pred)):

        if y_test[count] == y_pred[count]:
            correctly_classified = correctly_classified + 1

        if y_test[count] == y_pred1[count]:
            correctly_classified1 = correctly_classified1 + 1

        count = count + 1

    print("Accuracy on test set by our model	 : ", (
            correctly_classified / count) * 100)
    print("Accuracy on test set by sklearn model : ", (
            correctly_classified1 / count) * 100)


if __name__ == "__main__":
    main()
