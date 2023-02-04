#!/usr/bin/env python3
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#%%
def explained_variance():
    #%%
    
    data = pd.read_csv(r'src/data.tsv', sep='\t')
    pca = PCA(10)
    pca.fit(data)
    print(data.var().to_numpy())
    #print(np.var(data,axis=0))
        
        

    
    #%%
    return data.var().to_numpy(), pca.explained_variance_

def main():
    #%%
    v, ev = explained_variance()
    
    print(f"The variances are: {v[0]:.3f} {v[1]:.3f} {v[2]:.3f} {v[3]:.3f} {v[4]:.3f} {v[5]:.3f} {v[6]:.3f} {v[7]:.3f} {v[8]:.3f} {v[9]:.3f}")
    print(f"The explained variances after PCA are: {ev[0]:.3f} {ev[1]:.3f} {ev[2]:.3f} {ev[3]:.3f} {ev[4]:.3f} {ev[5]:.3f} {ev[6]:.3f} {ev[7]:.3f} {ev[8]:.3f} {ev[9]:.3f}")
    
    print(sum(v), sum(ev))
    
    plt.plot(np.arange(1,11), np.cumsum(ev));
    plt.show()
    
    #%%
if __name__ == "__main__":
    main()
