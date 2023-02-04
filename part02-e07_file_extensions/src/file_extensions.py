#!/usr/bin/env python3

def file_extensions(filename):
    with open(filename) as f:
        lines = f.readlines()
    a=[]
    b={}
    for line in lines:
        line=line.strip()
        if line.find('.')==-1:
            a.append(line)
            continue
        ext = line.split('.')[-1]
        if b.get(ext):
            b[ext].append(line)
        else:
            b[ext]=[line]
                
    print(a,b)

    return (a, b)
#%%
def main():
    #%%
    a,b = file_extensions('src/filenames.txt')
    print(f'{len(a)} files with no extension')
    for k in sorted(b.keys()):
        print(k, len(b[k]))
        
    
    
    #%%
    

if __name__ == "__main__":
    main()
    
    #%%