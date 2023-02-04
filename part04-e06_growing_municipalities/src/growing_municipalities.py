#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    
    return len(df[df.iloc[:,1]>0]) /len(df)
    
    
#%%
    
#%%
def main():
    #%%
    df=pd.read_csv(r'src/municipal.tsv',sep='\t',index_col='Region 2018')
    
    #%%
    p=growing_municipalities(df[20:30])*100
    print(f'Proportion of growing municipalities: {p:.1f}%')
    
    #%%
    return

if __name__ == "__main__":
    main()
