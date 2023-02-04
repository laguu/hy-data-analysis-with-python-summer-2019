#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
#%%
def subfigures(arr):
    fig, ax = plt.subplots(1,2)
    
    ax[0].plot(arr[:,0],arr[:,1])
    ax[1].scatter(arr[:,0],arr[:,1], c=arr[:,2], s=arr[:,3])
    
#    ax[0].plot(arr[0],arr[1])
#    ax[1].scatter(arr[0],arr[1], c=arr[2], s=arr[3])
    plt.show()
#%%
def main():
    #%%
    arr=np.array(([1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]))
#    print(arr)
    subfigures(arr)
#%%
if __name__ == "__main__":
    main()
