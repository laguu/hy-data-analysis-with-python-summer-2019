#!/usr/bin/env python3

import math
import numpy as np
#%%

def solve_quadratic(a, b, c):


    x1 = (-b+math.sqrt(b**2-4*a*c)) /2/a
    x2 = (-b-math.sqrt(b**2-4*a*c)) /2/a
    
    return (x1,x2)
#%%
#solve_quadratic(1,-3,2)
    

#%%
def main():
    solve_quadratic(1,-3,2)


   

if __name__ == "__main__":
    
    main()
