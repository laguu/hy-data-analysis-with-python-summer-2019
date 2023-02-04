#!/usr/bin/env python3

def find_matching(L, pattern):
    result=[]
    for i, val in enumerate(L):
#        print(i, val)
        if val.find(pattern)>-1:
            result.append(i)
            
    
    return result

#%%

#%%
def main():
#%%
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    # [0, 1, 3]

#%%
#    L=["sensitive", "engine", "rubbish", "comment"]
#    pattern= 'en'
#    result=list(map(lambda x: x.find(pattern) > -1, L))
#    print(result)
    
#%%

#%%
if __name__ == "__main__":
    main()
