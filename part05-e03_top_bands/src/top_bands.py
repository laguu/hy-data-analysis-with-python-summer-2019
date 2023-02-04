#!/usr/bin/env python3

import pandas as pd


#%%
def top_bands():
    #%%
    df = pd.read_csv('src/bands.tsv', '\t')
    df2 = pd.read_csv('src/UK-top40-1964-1-2.tsv', '\t')
    
    df2.Artist = df2['Artist'].str.title()
    df2.Title = df2['Title'].str.title()
    df2.Publisher = df2['Publisher'].str.title()

    res = pd.merge(df, df2, left_on='Band', right_on='Artist', how='left')
    
    return res
        
    
    #%%
def main():
    top_bands()

if __name__ == "__main__":
    main()
