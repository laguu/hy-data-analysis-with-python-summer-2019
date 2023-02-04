#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    unique, counts = np.unique(a[:,c], return_counts=True)
#    print(unique, counts)
    i=np.argsort(-counts)
#    print(i)
    r= np.concatenate([np.where(a[:,c]==unique[x])[0] for x in i])
#    print(r)
    
#    
#    for x in i:
#        f=np.where(a[:,c]==x)
#        print(f[0])
#        
        
        
#    print([np.concatenate((f,np.where(a[:,c]==x))) for x in i])
    
    return a[r]
#%%
def main():
    #%%
    np.random.seed(0)
    ar= np.random.randint(0, 10, (10,10))
    print(ar)
    most_frequent_first(ar, -1)
    
#%%
if __name__ == "__main__":
    main()
