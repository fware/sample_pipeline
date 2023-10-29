# My re-typing the simple linear regression model alg

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Linear Regression class
class LinearRegression():
	def __init__(self, lr, iter):
		self.lr = lr
		self.iter = iter


	# fit method for training
	def fit(self, x, y):
		# num of trainng examples, num of features
		self.m, self.n = x.shape

		# weight initialization
		self.w = np.zeros(self.n)
		self.b = 0
		self.x = x
		self.y = y

		# gradient descent
		for i in range(self.iter):
			self.update_weights()

		return self


	# update weights method
	def update_weights(self):
		y_pred = self.predict(self.x)

		# the gradient value
		dw = -1 * (2 * (self.x.T).dot(self.y - y_pred)) / self.m
		db = -2 * np.sum(self.y - y_pred) / self.m

		# update weights with gradients
		self.w = self.w - self.lr * dw
		self.b = self.b - self.lr * db

		return self

	# the predictor, in math terms it is the Hypothetical function h(x)
	def predict(self, x):
		v = x.dot(self.w) + self.b

		return v


def main():

	# load dataset
	# df = pd.read_csv("salary_data.csv")
	# df = pd.read_csv("diabetes.csv")
	df = pd.read_csv("car_data.csv")

	x_org = df.iloc[:, 2:3].values
	y_org = df.iloc[:, 4].values
	
	# x_org = df.iloc[:,:-1].values
	# y_org = df.iloc[:,1].values

	# split the dataset
	x_train, x_test, y_train, y_test = train_test_split(x_org, y_org, test_size=1/3, random_state=0)

	# create the model
	model = LinearRegression(iter=1000, lr=0.01)

	# train the model
	model.fit(x_train, y_train)

	y_pred = model.predict(x_test)

	# prediction results on test set
	print(f"Predicted values: {np.round(y_pred[:3], 2)}")
	print(f"Real values: {y_test[:3]} ")
	print(f"Trained W values: {round(model.w[0], 2)}")
	print(f"Trained b values: {round(model.b, 2)}")

	# scatter plot of test set
	plt.scatter(x_test, y_test, color="blue")
	plt.plot(x_test, y_pred, color="orange")

	# plt.title("Salary vs Experience")
	# plt.title("Age vs BMI")
	plt.title("Kms vs Selling Price")

	# plt.xlabel("Years of Experience")
	plt.xlabel("Price")

	# plt.ylabel("Salary")
	# plt.ylabel("Age")
	plt.ylabel("Kms Driven")

	plt.show()


if __name__ == "__main__":
	main()