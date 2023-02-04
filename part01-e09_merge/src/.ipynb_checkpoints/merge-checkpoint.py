#!/usr/bin/env python3

def merge(L1, L2):
    L3= []
    i=0
    j=0
    for c in range(len(L1)+len(L2)):
        if L1[i] > L2[j]:
            L3.append(L1[i])
            i=i+1
        else:
            L3.append(L2[j])
            j=j+1
            
        
    return L3

#%%
def main():
#%%
    merge([1,5,6],[2,3,4])

#%%
if __name__ == "__main__":
    main()
