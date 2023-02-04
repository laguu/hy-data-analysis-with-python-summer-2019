#!/usr/bin/env python3

import pandas as pd
import numpy as np
import re
#%%


def cleaning_data():
    #%%
    df=pd.read_csv('src/presidents.tsv', sep='\t')
    df.Start = df.Start.apply(lambda x: re.match(r'\d*',x).group(0))
    df.Seasons = df.Seasons.apply(lambda x: re.sub(r'two', '2', x))
    
    pres=df.President.str.split(expand=True)
    vice=df['Vice-president'].str.split(expand=True)
    
    pres[0]=pres[0].str.replace(r'\W',"")
    pres[1]=pres[1].str.replace(r'\W',"")
    vice[0]=vice[0].str.replace(r'\W',"")
    vice[1]=vice[1].str.replace(r'\W',"")
    pres[0]=pres[0].str.capitalize()
    pres[1]=pres[1].str.capitalize()
    vice[0]=vice[0].str.capitalize()
    vice[1]=vice[1].str.capitalize()
    
    pres.loc[[2,3], [0,1]] = pres.loc[[2,3], [1,0]].values
    vice.loc[[2,3], [0,1]] = vice.loc[[2,3], [1,0]].values
    vice
    
    vice=vice.apply(lambda x: " ".join(x), axis=1)
    pres=pres.apply(lambda x: " ".join(x), axis=1)
    df.President = pres
    df['Vice-president']= vice

    df.Start = df.Start.astype('int')
    df.Last = df.Last.apply(pd.to_numeric, errors='coerce')
    df.Seasons = df.Seasons.astype('int')
    df.dtypes
    
    
    return df
    


def main():
    return

if __name__ == "__main__":
    main()
