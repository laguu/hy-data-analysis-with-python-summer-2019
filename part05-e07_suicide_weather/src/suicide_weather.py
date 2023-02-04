#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    
    df = pd.read_csv('src/who_suicide_statistics.csv', sep=',')
    df['suicides'] = df.suicides_no / df.population
    
    df2 = df.groupby('country').mean()
    df2 = df2.drop(columns=['year','suicides_no','population'])
    
    return df2.suicides
#%%
def suicide_weather():
    suicides = pd.DataFrame(suicide_fractions())
    temps = pd.DataFrame(pd.read_html('src/List_of_countries_by_average_yearly_temperature.html')[0]).set_index('Country')
    temps.iloc[:,0] = temps.iloc[:,0].apply(lambda s: float(s.replace("\u2212", "-")))
    suicides.index = suicides.index.rename('Country')
    
    df = pd.merge(suicides, temps, left_on='Country', right_on='Country')
    
    spearman = df.iloc[:,0].corr( df.iloc[:,1], method='spearman')
    
    
    
    
    return (len(suicides), len(temps), len(df), spearman)

#%%
def main():
    #%%
    a,b,c,d = suicide_weather()
    
    print(f'Suicide DataFrame has {a} rows')
    print(f'Temperature DataFrame has {b} rows')
    print(f'Common DataFrame has {c} rows')
    print(f'Spearman correlation: {d}')
    
    
    #%%
    return

if __name__ == "__main__":
    main()
