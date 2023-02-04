#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    vals=s.data
    i=s.index
    
    
    r=pd.Series(i,index=vals,dtype=i.dtype)
    
    
    
    return r
#%%
def main():
    #%%
    s1=pd.Series([1, 2, 3, 1], index=['a', 'b', 'c', 'd'])
    print(s1)
    print(inverse_series(s1))
    
#%%
if __name__ == "__main__":
    main()
