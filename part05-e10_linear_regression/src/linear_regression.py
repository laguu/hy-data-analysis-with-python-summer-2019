#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis], y)
    
    return model.coef_[0], model.intercept_
    
def main():
    x = np.arange(5)
    y = np.arange(5)/3+1
    a, b = fit_line(x,y)
    
    print('Slope:', a)
    print('Intercept:', b)
    
    
    plt.scatter(x,y)
    plt.plot()
    plt.show()
    return
    
    
if __name__ == "__main__":
    main()
