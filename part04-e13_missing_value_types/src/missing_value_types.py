#!/usr/bin/env python3

import pandas as pd
import numpy as np
#%%
def missing_value_types():
    #%%
    df=pd.DataFrame([['United Kingdom',None,None],['Finland',1917,'Niinistö'],['USA',1776,'Trump'],['Sweden',1523,None],['Germany',None,'Steinmeier'],['Russia',1992,'Putin']])
    df.columns=['State','Year of independence','President']
    df=df.set_index('State', drop=True)
    return df


#%%
    return None
               
def main():
    return

if __name__ == "__main__":
    main()
