#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a):
    y=(a.shape[0]-1) /2.0
    x=(a.shape[1]-1) /2.0

    return (y,x)
    
"""
def center(a):
    print(a.shape)
    if a.shape[0]==1:
        ymid=1
    else:
        ymid=(a.shape[0])/2.0+0.5
    if a.shape[1]==1:
        xmid=1
    else:
        xmid=(a.shape[1])/2.0+0.5
    print(ymid,xmid)
    return (ymid,xmid)
#    return (0,0)   # note the order: (center_y, center_x)
"""
def radial_distance(a):
    c=center(a)
    y=c[0]-np.arange(a.shape[0])
    x=c[1]-np.arange(a.shape[1])
    x=x.reshape(1,x.shape[-1])
    y=y.reshape(y.shape[-1],1)
    res= np.sqrt(x**2+y**2)
    return res

def scale(a, tmin=0.0, tmax=1.0):
    arr=a.copy()
    if (arr.shape[0]==1) & (arr.shape[1]==1):
        if arr.max==0:
            return 1-arr
        else:
            return arr/arr.max()*tmax
    arr=arr-arr.min()
    arr=arr/arr.max()
    arr=arr*(tmax)+tmin
    return arr
    
def radial_mask(a):
    mask=1-scale(radial_distance(a))
#    print(mask.min(), mask.max())
#    mask=np.clip(mask,0,1)
    return mask
    
def radial_fade(a):
    mask=radial_mask(a)
    assert(mask.max()==1)
#    mask=mask.reshape(mask.shape[0],mask.shape[1],1)
    mask=np.expand_dims(mask,2)
    return a.copy()*mask



#%%
def main():
    #%%
    a=np.array([[[1,1,1]]])*3.44
    b=np.arange(1,28).reshape(3,3,3)
    c=np.arange(1,26).reshape(5,5)
    img=plt.imread(r'src/painting.png')
       
    img=b
    fig,ax=plt.subplots(3)
    ax[0].imshow(img)
    ax[1].imshow(radial_mask(img))
    ax[2].imshow(radial_fade(img))
    plt.show()
    
    

#%%
if __name__ == "__main__":
    main()
#%%
##    a=np.eye(1)*3.44
#    b=np.arange(1,17).reshape(4,4)
#    c=np.arange(1,26).reshape(5,5)
    scale(a)

#%%
scale(np.array([[[45]]]))


