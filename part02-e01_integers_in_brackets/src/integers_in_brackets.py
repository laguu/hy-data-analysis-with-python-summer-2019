#!/usr/bin/env python3
import re

def integers_in_brackets(s):
#    result=re.findall(r"\[[^\[\]]*\]",s)
    result=re.findall(r'\[\s*([+-]?\d+)\s*\]',s)
    print(result)
    t=list(map(int, result))
    return t
    
#%%
def main():
    
    #%%
    integers_in_brackets("  afd [128+][asd] [12 ] [a34]  [ +-43 ]tt [+12]xxx")


#%%
if __name__ == "__main__":
    main()
