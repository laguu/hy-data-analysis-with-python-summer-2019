#!/usr/bin/env python3
import pandas as pd

def read_series():
    i=[]
    vals= []
    c=True
    while c:
        new=input()
        if new=="":
            c=False
        else:
            newi, newval = new.split()
            i.append(newi)
            vals.append(newval)
    result=pd.Series(vals)
    result.index=i
    return result

#%%
def main():
    #%%
    read_series()


#%%
if __name__ == "__main__":
    main()
