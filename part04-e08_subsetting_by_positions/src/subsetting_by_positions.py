#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    #%%
    df=pd.read_csv(r'src/UK-top40-1964-1-2.tsv', sep='\t')
    return df.iloc[0:10,2:4]
    
    
    #%%

def main():
    subsetting_by_positions()

if __name__ == "__main__":
    main()
