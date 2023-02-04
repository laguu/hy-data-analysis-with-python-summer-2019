#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename) as f:
        lines = f.readlines()
    a=len(lines)
    
    words=[]
    for line in lines:
        words+=line.split()
    b=len(words)
    chars=0
    for word in lines:
        chars+=len(word)
    
    
    return (a, b, chars)

#%%
def main():
    #%%
    
    for file in sys.argv[1:]:
        a,b,c = file_count(file)
        print(f'{a}\t{b}\t{c}\t{file}')
        
        
   #%% 
if __name__ == "__main__":
    main()
    
    
#%%
#file=r'src\test.txt'
#a,b,c=    file_count(file)
#print(f'{a}\t{b}\t{c}\t{file}')
