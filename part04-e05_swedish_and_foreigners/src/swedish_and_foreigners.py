#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    #%%
    df=pd.read_csv(r'src/municipal.tsv',sep='\t',index_col='Region 2018')
    #%%
    df=df[1:312]
    df=df[df.iloc[:,3]>5]
    df=df[df.iloc[:,2]>5]
    df=df.iloc[:,[0,2,3]]
    #%%
    return df

def main():
    swedish_and_foreigners()

if __name__ == "__main__":
    main()
#%%
    df.columns