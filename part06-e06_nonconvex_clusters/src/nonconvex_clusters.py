#!/usr/bin/env python3
import scipy

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

#%%
def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    #%%
    data = pd.read_csv(r'src/data.tsv', sep='\t')
    X = data[['X1','X2']]
    y = data['y']
    
    
    #%%
    
    result = []
    for eps in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=eps)
        model.fit(X)
        
        clusters = len(set(model.labels_)) - (1 if -1 in model.labels_ else 0)
        permutation = find_permutation(clusters, y, model.labels_)
        
        new_labels = np.array([permutation[label] for label in model.labels_])
        
        mask = new_labels != -1
        # print(mask)
        accuracy = accuracy_score(y[mask], new_labels[mask])
        
        if clusters != len(y):
            accuracy == np.nan
        
        outliers = len(model.labels_[model.labels_==-1])
        result.append([eps,accuracy,clusters,outliers])
        
    result = pd.DataFrame(np.array(result), columns=['eps' ,  'Score',  'Clusters',  'Outliers'])
    #%%
    
    return result
    
    
    
    
    
    
    
    #%%
    return pd.DataFrame()

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
