#!/usr/bin/env python3

def mul(tpl):
    res=1
    for val in tpl:
        res=res*val
    return res


def transform(s1, s2):
    if s1=='' or s2=='':
        return []
    
    print(s1,len(s1))
    print(s2,len(s2))

    i1= list(map(int, s1.split(' ')))
    i2= list(map(int, s2.split(' ')))
    t=list(zip(i1 , i2))
    
    result= list(map(mul, t))
    
    
    return result


#%%
#    transform("1 5 3", "2 6 -1")
    
#%%
def main():
    transform("1 5 3", "2 6 -1")
#%%
if __name__ == "__main__":
    main()
