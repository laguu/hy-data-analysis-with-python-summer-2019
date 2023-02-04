#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    L=[]
    for row in a:
        L.append(row)
    return L
        
    
def get_columns(a):
    L=[]
    for row in a.T:
        L.append(row)
    return L

def main():
    pass
    #%%
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))
#%%
if __name__ == "__main__":
    main()
