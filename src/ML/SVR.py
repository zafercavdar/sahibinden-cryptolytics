from sklearn.svm import SVR
import numpy as np


def SVR_rbf(X, y):
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    X = np.array(X).reshape(-1, 1)
    y = np.array(y)
    model = svr_rbf.fit(X, y)
    return model
