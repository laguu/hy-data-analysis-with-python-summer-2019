#!/usr/bin/env python3

def word_frequencies(filename):
    with open(filename) as f:
        lines=f.readlines()
    words=[]
    for line in lines:
        words=words+line.split()
    words = list(map(lambda x: x.strip("""!"#$%&'()*,-./:;?@[]_"""), words))
    
    new={}
    for v in words:
        if new.get(v):
            print(f'{v} exists, add +1')
            new[v]+=1
        else:
            print(f'{v} doesn\'t exist, add key')
            new[v]=1                                     
    return new

#%%
def main():
    pass

if __name__ == "__main__":
    main()
#%%
    
    
#    word_frequencies('alice.txt') 