#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    i=np.arange(n).reshape(1,n)
    j=np.arange(n).reshape(n,1)
    return i*j
    
    #%%
    
def main():
    #%%
    print(multiplication_table(4))
#%%
if __name__ == "__main__":
    main()
