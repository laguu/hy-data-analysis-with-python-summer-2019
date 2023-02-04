#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
#%%
def to_grayscale(image):
    gimage = 0.2126*image[:,:,0]+ 0.7152*image[:,:,1]+ 0.0722*image[:,:,2]
    print(gimage.shape)
    return gimage

def to_red(image):
    img=image.copy()
    img[:,:,[1,2]]=0
    return img

def to_green(image):
    img=image.copy()
    img[:,:,[0,2]]=0
    return img

def to_blue(image):
    img=image.copy()
    img[:,:,[0,1]]=0
    return img


#%%
def main():
    #%%
    img=plt.imread(r'src/painting.png')
    plt.imshow(to_grayscale(img))
    plt.gray()
    plt.show()
#    plt.imshow(img)
#    plt.show()
    fig, (ax1,ax2,ax3)=plt.subplots(3)
    ax1.imshow(to_red(img))
    ax2.imshow(to_green(img))
    ax3.imshow(to_blue(img))
    plt.show()
    
    
    #%%

if __name__ == "__main__":
    main()
