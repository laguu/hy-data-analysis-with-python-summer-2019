#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(a**2, axis=1))

def main():
    #%%
    m=np.arange(15).reshape(3,5).T
    vector_lengths(m)
    #%%
if __name__ == "__main__":
    main()
