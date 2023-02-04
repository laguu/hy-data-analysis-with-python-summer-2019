#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

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
def days(s):
    return wd[s]

def months(s):
    return m[s]
    

#%%


def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]

    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(axis=0, how='all')
    df = df.dropna(axis=1, how='all')
    df = pd.concat((split_date(df), df.drop(columns=['Päivämäärä'])), axis=1)
    
    return df
#%%




def cyclists_per_day():
    #%%
    df = split_date_continues()
    df = df.groupby(['Year','Month','Day']).sum()
    df = df.drop(columns=['Hour'])
    return df
    
    
    
    
    #%%
    
def main():
    df = cyclists_per_day()
    df.plot()
    plt.show()
    
    return

if __name__ == "__main__":
    main()
