import os
#%%
#!/usr/bin/env python3

def detect_ranges(L):
    K= L.copy()
    K.sort()
    
    intervals=[]
    x=0
    i=0
    
    while x<len(K):
        while K[x+i+1] - K[x+i] == 1:
            i+=1
            if x+i>=len(K)-1:
                break
        
        if i==0:
            intervals.append(K[x])
        if i>0:
            intervals.append((K[x], K[x+i]+1))
        x=x+i+1
        i=0
        
    return intervals
    
#%%
def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

#%%
if __name__ == "__main__":
    main()

#%%
#L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
#result = detect_ranges(L)
#print(L)
#print(result)
