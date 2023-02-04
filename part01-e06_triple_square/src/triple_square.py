#!/usr/bin/env python3

def triple(x):
    return 3*x

def square(x):
    return x**2

#%%

def main():
    #%%
    for i in range(1,11):
        a=triple(i)
        b=square(i)
        if a<b:
            break
        print('triple({})=={} square({})=={}'.format(i,a,i,b))
    



#%%
if __name__ == "__main__":
    main()


#%%
    
