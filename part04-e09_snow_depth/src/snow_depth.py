#!/usr/bin/env python3

import pandas as pd
#%%
def snow_depth():
    
    df=pd.read_csv(r'src/kumpula-weather-2017.csv',sep=',')
    return df['Snow depth (cm)'].max()
#%%
def main():
    #%%
    d=snow_depth()
    print(f'Max snow depth: {d:.1f}')
#%%
if __name__ == "__main__":
    main()
