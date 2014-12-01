import numpy as np

def colvec(X):
    return np.reshape(X, (-1,1))

def repeat_column(X, n):
    return np.repeat(X, n, axis=1)
