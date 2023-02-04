#!/usr/bin/env python3
import pandas as pd


def create_series(L1, L2):
    idx=['a','b','c']
    s1=pd.Series(L1,index=idx)
    s2=pd.Series(L2,index=idx)
    return (s1, s2)
    
def modify_series(s1, s2):
    s1.at['d']=s2['b']
    del s2['b']
    print(s1,s2)

    return (s1, s2)
    
#%%
def main():
    #%%
    ss1, ss2 =create_series([1,2,3],[34,65,22])
    print(ss1,ss2)
    ss1, ss2 =modify_series(ss1,ss2)
    print(ss1+ss2)




    #%%
if __name__ == "__main__":
    main()
