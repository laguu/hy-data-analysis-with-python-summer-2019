#!/usr/bin/env python3

import pandas as pd
#%%
def main():
    #%%
   df=pd.read_csv(r'src/municipal.tsv', sep='\t')
   print(f'Shape: {df.shape[0]},{df.shape[1]}')
   print('Columns:')
   [print(c) for c in df.columns]




#%%
if __name__ == "__main__":
    main()
