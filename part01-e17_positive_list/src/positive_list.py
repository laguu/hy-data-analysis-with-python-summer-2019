#!/usr/bin/env python3

def positive_list(L):
    f = list(filter(lambda x: x>0, L))
    return f

#%%
def main():
    #%%
    positive_list([2,-2,0,1,-7])
#    [2,1]

#%%
if __name__ == "__main__":
    main()
