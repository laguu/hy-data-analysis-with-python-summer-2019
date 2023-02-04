#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

#%%
# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines
#%%
 
def get_features(a):
    return np.char.count(a, np.array(list(alphabet)).reshape(len(alphabet),1)).T


#%%

def contains_valid_chars(s):
    return not bool(set(s).difference(alphabet_set))

#%%
def get_features_and_labels():
    
    fin = np.array(load_finnish())
    fin = np.char.lower(fin)
    fin = fin[np.vectorize(contains_valid_chars)(fin)]
    fin
    
    eng = np.array(list(load_english()))
    eng = eng[~np.vectorize(lambda x: x[0].isupper())(eng)]
    eng = np.char.lower(eng)
    eng = eng[np.vectorize(contains_valid_chars)(eng)]
    
    X = np.vstack(  (get_features(fin),get_features(eng))  )
    
    y = np.hstack((np.zeros(len(fin), dtype=int),np.ones(len(eng), dtype=int)))

    return X, y
#%%

def word_classification():
    
    X, y = get_features_and_labels()
    
    model = MultinomialNB()
    model.fit(X,y)

    return cross_val_score(model, X, y, cv=model_selection.KFold(n_splits=5, shuffle=True, random_state=0)).tolist()

#%%
def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
#%%
X, y= get_features_and_labels()
#%%
y.shape




