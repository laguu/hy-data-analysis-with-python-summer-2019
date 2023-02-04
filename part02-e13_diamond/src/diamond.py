#!/usr/bin/env python3

import numpy as np

def diamond(n):
#    i=int(n//2)
#    if n%2==0:
#        a=np.eye(i,dtype=int)
#        b=np.concatenate((np.flip(a,axis=1), a), axis=1)
#        c=np.concatenate((b, np.flip(b,axis=0)), axis=0)
#    else:
    a=np.eye(n, dtype=int)
    b=np.concatenate((np.flip(a,axis=1)[:,:-1], a), axis=1)
    c=np.concatenate((b[:-1,:], np.flip(b,axis=0)), axis=0)
        
    return c
    
#%%
def main():
    pass

if __name__ == "__main__":
    main()
#%%
    diamond(2)
#%%
    type(int(6/2))