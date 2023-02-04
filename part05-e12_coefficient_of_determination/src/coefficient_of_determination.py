#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import linear_model

#%%
def coefficient_of_determination():
    #%%
    df = pd.read_csv('src/mystery_data.tsv', '\t')
    model = linear_model.LinearRegression(fit_intercept=True)
    L = df.shape[-1]
    score = []
    
    #%%
#    model.fit(X[:,np.newaxis],y[:,np.newaxis])
#    score.append(model.score(X,y)[0])

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    model.fit(X,y[:,np.newaxis])
    score.append(model.score(X,y))

    for i in range(L-1):
        X = df.iloc[:, i]
        y = df.iloc[:,-1]
        model.fit(X[:,np.newaxis],y[:,np.newaxis])
        score.append(model.score(X[:,np.newaxis],y[:,np.newaxis]))

    return score
    #%%
    
    
def main():
    #%%
    coeff = coefficient_of_determination()
    print(coeff)
    
#%%
if __name__ == "__main__":
    main()

#
#
##%%
#def mystery_data():
#
#    return model.coef_
##%%
#def main():
#    #%%
#    coefficients = mystery_data()
#    for i, c in enumerate(coefficients):
#        print(f'Coefficient of X{i+1} is {c}')
#        
    
#%%

    