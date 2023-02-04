#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    l=a.shape[1]//2
    c=np.sum(a[:,:l], axis=1) > np.sum(a[:,l:], axis=1)
    print(c)
    
    return a[c]
#%%
def main():
    #%%
    np.random.seed(0)
    ar=np.random.randint(0,20,(5,10))
    print(ar)
    first_half_second_half(ar)
#%%
if __name__ == "__main__":
    main()
