#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    #%%
    df=pd.read_csv(r'src/municipal.tsv', sep='\t', index_col='Region 2018')
    return df.loc['Akaa':'Äänekoski', ['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    
    
    #%%
    return None

def main():
    return

if __name__ == "__main__":
    main()
