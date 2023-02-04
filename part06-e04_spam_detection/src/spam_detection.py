#!/usr/bin/env python3
import gzip
import numpy as np

#%%

def spam_detection(random_state=0, fraction=1.0):
    #%%
    with gzip.open(r'src/ham.txt.gz', 'r') as f:
        lines = np.array(f.readlines())
    lines=np.str(lines)
    lines
    # Jatka tästä
    
    #%%
    return 0.0, 0, 0

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
#%%

    