#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
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

def days(s):
    return wd[s]

def months(s):
    return m[s]
    




def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]
    d['Min'] = hourmin.iloc[:, 1]

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


def bicycle_timeseries():
    
    df = split_date_continues()
    df.Min = pd.to_numeric(df.Min)
    
    df['Päivämäärä'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour']])
    df = df.set_index('Päivämäärä')
    df = df.drop(columns=['Weekday', 'Day', 'Month', 'Year', 'Hour', 'Min'])
    df
    
    
    return df
    #%%


def commute():
    
    df = bicycle_timeseries()
    df = df['2017-08']
    df['Weekday'] = df.index.weekday+1
    df = df.set_index('Weekday')
    df = df.groupby('Weekday').sum()
    print(df.index)
    return df
    
    #%%
def main():
    #%%
    df = commute()
    df.plot()
    weekdays="mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()

    #%%
    return


if __name__ == "__main__":
    main()
