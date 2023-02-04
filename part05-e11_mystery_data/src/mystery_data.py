#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
#%%
def mystery_data():
    
    df = pd.read_csv('src/mystery_data.tsv', '\t')
    model = LinearRegression(fit_intercept=False)
    model.fit(df.iloc[:, :5], df.iloc[:, 5])
    
    
    return model.coef_
#%%
def main():
    #%%
    coefficients = mystery_data()
    for i, c in enumerate(coefficients):
        print(f'Coefficient of X{i+1} is {c}')
        
    
    
    
    #%%
if __name__ == "__main__":
    main()
