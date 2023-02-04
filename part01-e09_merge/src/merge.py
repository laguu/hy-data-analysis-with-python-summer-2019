#!/usr/bin/env python3

def merge(L1, L2):
    L= L1.copy() + L2.copy()

    for c in range(len(L)):
        low= c
        i= c+1
        while i<len(L):
            if L[i] < L[low]:
                low=i
            i=i+1
        temp=L[c]
        L[c]=L[low]
        L[low]=temp
        
    return L

 
#%%
def main():
    L1=[1,2,4,7,8]
    L2=[0,5,6,9]
    merge(L1,L2)
#%%

    #%%
if __name__ == "__main__":
    main()
