#!/usr/bin/env python3

import pandas as pd
import re
#%%
def municipalities_of_finland():
    #%%
    df=pd.read_csv(r'src/municipal.tsv',sep='\t',index_col='Region 2018')
    df=df[1:312]

    return df
    

#%%
def main():
    municipalities_of_finland()
    
if __name__ == "__main__":
    main()
