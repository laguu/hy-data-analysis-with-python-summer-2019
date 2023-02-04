#!/usr/bin/env python3

def reverse_dictionary(d):
    new={}
    for k in d.keys():
        for v in d[k]:
            if new.get(v):
                print(f'{v} exists, append {k}')
                new[v].append(k)
            else:
                print(f'{v} doesn\'t exist, add list [{k}]')
                new[v]=[k]
    return new
#%%
    
#%%
def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)


if __name__ == "__main__":
    main()
