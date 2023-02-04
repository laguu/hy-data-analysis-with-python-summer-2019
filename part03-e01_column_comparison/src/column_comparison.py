#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    c=a[:,1]>a[:,-2]
    return a[c]
   #%% 
def main():
    #%%
    ar=np.random.randint(0,20,(5,5))
    print(ar)
    column_comparison(ar)
#%%
if __name__ == "__main__":
    main()
