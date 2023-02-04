#!/usr/bin/env python3

import pandas as pd
import numpy as np
import re
#%%
def check(s):
    lambda x: if (x=='Re')|(x=='New')  

def special_missing_values():
    #%%
    df=pd.read_csv(r'src/UK-top40-1964-1-2.tsv', sep='\t')
#    ~df['LW'].apply(lambda txt: bool(re.search(r'Re|New', txt)))
    mask=df['LW'].str.contains('Re|New', regex=True)
    df['LW'][mask]=None
    df['LW']=df['LW'].astype('float')
    df['Pos']=df.Pos.astype('float')
    return df[df.Pos>df.LW]
    
    #%%

def main():
    return

if __name__ == "__main__":
    main()
