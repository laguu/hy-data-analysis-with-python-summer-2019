#!/usr/bin/env python3

import pandas as pd
#%%
def below_zero():
    
    df=pd.read_csv(r'src/kumpula-weather-2017.csv')
    df['Below Zero'] = df.iloc[:,-1].apply(lambda x: x<0)
    return df['Below Zero'].value_counts()[True]
    
    #%%
    
def main():
    #%%
    d=below_zero()
    print(f'Number of days below zero: {d:.1f}')
    
    #%%
if __name__ == "__main__":
    main()
