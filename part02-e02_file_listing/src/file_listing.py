#!/usr/bin/env python3

import re
import os
#%%
#os.chdir('E:\\koodit\\hy-data-analysis-with-python-summer-2019\\part02-e02_file_listing')


#%%
def file_listing(filename="src/listing.txt"):
    l= []
    with open(filename) as f:
        for line in f:
            #res=re.finditer(r'\d+|[A-Z][a-z]{2}\b|\w+.\w+$', line[12:])
            res=re.finditer(r'[\.\-A-Za-z0-9_]+', line[30:])
            
            
            L=[]
            
            for j in res:
                s=j.group()
                try:
                    s=int(s)
                except:
                    pass
                L.append(s)
            l.append(tuple(L))
    return l

#%%
def main():
#%%
    file_listing()



#%%
if __name__ == "__main__":
    main()

#%%
    s='234'
    try:
        s=int(s)
    except:
        pass
    s