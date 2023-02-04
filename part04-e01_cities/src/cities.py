#!/usr/bin/env python3

import pandas as pd

def cities():
#%%            
    df=pd.DataFrame([[643272     ,715.48],[279044  ,528.03],[231853 ,689.59],[223027 ,240.35],[201810  ,3817.52]])
    i=pd.Series(['Helsinki','Espoo','Tampere','Vantaa','Oulu'])
    df=df.set_index(i)
    df.columns=['Population', 'Total area']
    return(df)
    
    
#%%

    
#%%
def main():
   #%%
    return
    #%%
if __name__ == "__main__":
    main()
