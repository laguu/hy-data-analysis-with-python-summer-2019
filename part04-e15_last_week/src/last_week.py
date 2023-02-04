#!/usr/bin/env python3

import pandas as pd
import numpy as np
#%%
def last_week():
    #%%
    df=pd.read_csv(r'src/UK-top40-1964-1-2.tsv', sep='\t')
    df[['Pos','LW','Peak Pos','WoC']]=df[['Pos','LW','Peak Pos','WoC']].apply(pd.to_numeric, errors='coerce')
    df['WoC'] = df.WoC-1
    df[df.Pos==df['Peak Pos']]['Peak Pos']=np.nan
    
    
    new=pd.DataFrame(df.Pos)
    df['Pos']=df.LW
    df['LW']=np.nan
    
    df=df.sort_values(by='Pos')
    result=new.set_index('Pos').join(df.set_index('Pos'), how='left', lsuffix='-l', rsuffix='-r').reset_index()
    result.loc[[5,8,14,15,22,26,28,31], 'Peak Pos'] = np.nan
#    result.loc[8, 'Peak Pos'] = np.nan
    
    

  #%%  
    return result



    
    
#%%
def main():
    
    #%%
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)

#%%
if __name__ == "__main__":
    main()
