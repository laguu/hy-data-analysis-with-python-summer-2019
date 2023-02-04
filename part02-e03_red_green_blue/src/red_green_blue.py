#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    first=True
    with open(filename) as f:
        lines = f.readlines()
    L=[]
    for line in lines:
        if first:
            first=False
            continue
        r=re.findall(r'\d{1,3}|\b[A-Za-z0-9_ ]+$', line)    
        L.append("\t".join(r))
    return L

#%%
def main():
#%%
    print(red_green_blue())


#%%
if __name__ == "__main__":
    main()
