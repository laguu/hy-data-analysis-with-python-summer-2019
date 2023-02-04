#!/usr/bin/env python3

import pandas as pd
#%%
def average_temperature():
    
    df=pd.read_csv(r'src/kumpula-weather-2017.csv')
    means=df.groupby('m').mean()
    return means.iloc[6,-1]
    
#%%
def main():
    #%%
    m=average_temperature()
    print(f'Average temperature in July: {m:.1f}')



#%%
if __name__ == "__main__":
    main()
