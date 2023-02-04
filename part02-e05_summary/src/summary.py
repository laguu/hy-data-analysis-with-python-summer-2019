#!/usr/bin/env python3

import sys
import numpy as np

def summary(filename):
    with open(filename) as f:
        lines=f.readlines()
    L=[]
    for row in lines:
        try:
            L.append(float(row))
        except:
            pass
        
    a = sum(L)
    b = a/len(L)
    c = np.sqrt(np.sum(np.array([i-b for i in L])**2)/(len(L)-1))
    
    return(a,b,c)
#%%
def main():
    for file in sys.argv[1:]:
        a,b,c = summary(file)
        print(f'File: {file} Sum: {a:.6f} Average: {b:.6f} Stddev: {c:.6f} ')

if __name__ == "__main__":
    main()
#%%
    summary('example.txt')