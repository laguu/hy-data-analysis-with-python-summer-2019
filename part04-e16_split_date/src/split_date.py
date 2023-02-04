#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os
os.getcwd()
#%%
wd = {
    'ma' : 'Mon',
    'ti' : 'Tue',
    'ke' : 'Wed',
    'to' : 'Thu',
    'pe' : 'Fri',
    'la' : 'Sat',
    'su' : 'Sun'
}


m = {
    'tammi': 1,
    'helmi': 2,
    'maalis': 3,
    'huhti': 4,
    'touko': 5,
    'kesä': 6,
    'heinä': 7,
    'elo': 8,
    'syys': 9,
    'loka': 10,
    'marras': 11,
    'joulu': 12
}

#%%
def split_date():
#%%
    df = pd.read_csv(r'src/Helsingin_pyorailijamaarat.csv', sep=';')
    df=df.dropna(axis=0, how='all')
    df=df.dropna(axis=1, how='all')
    new = pd.DataFrame(df['Päivämäärä'].str.split(expand=True))
    new.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    new.Month = pd.to_numeric(new.Month.apply(lambda x: m[x]))
    new.Weekday = new.Weekday.apply(lambda x: wd[x])
    new.Hour = pd.to_numeric(new.Hour.str.slice(0,2))
    new.Day = pd.to_numeric(new.Day)
    new.Year = pd.to_numeric(new.Year)
    new    
    #%%
    return new

#%%
def main():
    split_date()
    
    return
       
if __name__ == "__main__":
    main()
