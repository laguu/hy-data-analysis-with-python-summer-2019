#!/usr/bin/env python3

import pandas as pd
#%%
def cyclists():
    #%%
    df=pd.read_csv(r'src/Helsingin_pyorailijamaarat.csv', sep=';')
    df=df.dropna(axis=0, how='all')
    df=df.dropna(axis=1, how='all')
    return df
    


#%%
def main():
    return
    
if __name__ == "__main__":
    main()
