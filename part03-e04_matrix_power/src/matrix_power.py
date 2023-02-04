#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    size=a.shape[0]
    if n==0:
        return np.eye(size)
    
    if n<0:
        a=np.linalg.inv(a)
    
    n=np.abs(n)
    t=[a] * n
    
    res= reduce(lambda x,y: x@y, t, np.eye(size))
    return res


#%%
def main():
    #%%
    np.random.seed(0)
    a=np.random.rand(1, 4).reshape(2,2)
#    print(a@a@a)
    matrix_power(a,3)
    #%%

if __name__ == "__main__":
    main()
#%%
