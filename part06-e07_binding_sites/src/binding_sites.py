#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc
import scipy

mapping={ 'A': 0, 'C': 1, 'G': 2, 'T': 3 }
# filename=r'data.seq'
#%%
def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


#%%
def toint(x):
    return mapping[x]
#%%
def get_features_and_labels(filename):
    
    df = pd.read_csv(filename, sep='\t')
    features = pd.DataFrame(df.X.map(list).tolist())
    features = features.applymap(toint).values#.tolist()
    # print(df.y.values)
    # print(pd.DataFrame(df.X.map(list).tolist()).applymap(toint))
    
    return (features, df.y.values)
#%%
def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()
#%%
def cluster_euclidean(filename):
   
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(2, linkage='average',affinity='euclidean')
    model.fit(X)
    
    permutations = find_permutation(2, y, model.labels_)
    new_labels = np.array([permutations[l] for l in model.labels_])

    print(new_labels)
    accuracy = accuracy_score(y, new_labels)
    
    # plot(pairwise_distances(X))

    return accuracy
#%%
def cluster_hamming(filename):
    #%%
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(2, linkage='average',affinity='precomputed')
    y_pred = model.fit_predict(pairwise_distances(X, metric='hamming'))
    
    permutations = find_permutation(2, y, y_pred)
    new_labels = np.array([permutations[l] for l in y_pred])
    
    accuracy = accuracy_score(y, new_labels)
    
    # plot(pairwise_distances(X))
    
    #%%
    return accuracy


def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
