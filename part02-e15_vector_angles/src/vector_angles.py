#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    XY=np.sum(X*Y)
    XX=np.sqrt(np.sum(X**2))
    YY=np.sqrt(np.sum(Y**2))
    print(XY,XX,YY)

    return np.arccos(XY/XX/YY)/np.pi*180
    
    
    
    
#%%
def main():
    #%%
    vector_angles(np.array([3,4,5],), np.array([-2,3.4,1.6]))
    
    #%%
if __name__ == "__main__":
    main()
    
    
    #%%
    i=12
    a=np.arange(i).reshape(3,i//3)
    b=np.arange(i).reshape(3,i//3).T
    print(np.arange(5).reshape(1,5).T)
    print(b)
    
    np.dot(a.T,a)