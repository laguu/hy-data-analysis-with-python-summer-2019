#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model

#%%
def coefficient_of_determination():
    
    df = pd.read_csv('src/mystery_data.tsv', '\t')
    # df.iloc[:,list(set([1,2,3]))]
    model = linear_model.LinearRegression(fit_intercept=True)

    L = df.shape[-1]
    score = []
    
    for i in range(L):
        cols = list( set(range(5)).difference([i]) )
        X=df.iloc[:,cols]
        y=df.iloc[:,i]
        model.fit(X, y)
        
        score.append(model.score(X,y))
        
    return score
    #%%
    
    
def main():
    coeff = coefficient_of_determination()
    print(coeff)
    

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

    