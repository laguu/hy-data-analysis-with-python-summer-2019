#!/usr/bin/env python3

import pandas as pd
import numpy as np

def powers_of_series(s, k):
    df=pd.DataFrame()
    cols=np.arange(1,k+1)
    for i in cols:
        df=pd.concat((df, s**i), axis=1, sort=True)
        
    df.columns=cols
    return df
    
    
    
    

#%%    
def main():
    #%%
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 6))

   
    #%%
    return
    
if __name__ == "__main__":
    main()
