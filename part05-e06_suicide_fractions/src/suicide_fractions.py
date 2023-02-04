#!/usr/bin/env python3

import pandas as pd

#%%
def suicide_fractions():
    #%%
    df = pd.read_csv('src/who_suicide_statistics.csv', sep=',')
    df['suicides'] = df.suicides_no / df.population
    
    df2 = df.groupby('country').mean()
    df2 = df2.drop(columns=['year','suicides_no','population'])
    
    #%%
    return df2.suicides

def main():
    suicide_fractions()
    return

if __name__ == "__main__":
    main()
