import data as dc
from wrappers import debug
import config

from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

import pickle as p
import numpy as np
import os

@debug
def train(trainFeature, trainCost):
	"""
	Creates a model and trains it with the training features and costs
	"""
	model = RandomForestRegressor()
	model.fit(trainFeature, trainCost)
	return model

@debug
def predict(model, testFeature, testCost):
	"""
	Uses a modle and predicts the cost given the test features. 
	Returns the accuracy score
	"""
	predicts = model.predict(testFeature)
	with open("predictions.txt", 'wb') as f:
		p.dump(predicts, f)
	return metrics.mean_absolute_error(testCost, predicts)

@debug
def loadData(filename, test = .1):
	"""
	Loads data from .npy binaries representative of our data created by format_data.py
	Takes in filename (i.e. 144d.dat) and a test size (percentage)
	returns trainX, trainY, testX, testY
	"""
	X = np.load(os.path.join("..","data",filename[:-4] + "_dataX.npy"))
	Y = np.load(os.path.join("..","data",filename[:-4] + "_dataY.npy"))
	cut = int(X.shape[0] * test)
	return  X[cut:], Y[cut:], X[:cut], Y[:cut]

if __name__ == "__main__":
	trainFeature, trainCost, testFeature, testCost = loadData(config.H144D)

	# print trainFeature.shape
	# print trainCost.shape

	# print testFeature.shape
	# print testCost.shape

	model = train(trainFeature, trainCost)
	error = predict(model, testFeature, testCost)

	print error # Currently only around 1000 dollars


