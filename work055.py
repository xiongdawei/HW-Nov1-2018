#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 23:40:33 2018

@author: davidxiong
"""
import numpy as np
def create_square(n):
    if n%2==0:
        print('This magic square cannot be generated')
    else:
        square = np.zeros((n,n))
        a,b = 0, n//2
        index = 1
        square[a][b] = index
        print(square)
        while index<n**2:
            if 0<a and b<n-1:
                if square[a-1][b+1]==0:
                    a-=1
                    b+=1
                    index+=1
                    square[a][b]=index
                    
                else:
                    a+=1
                    index+=1
                    square[a][b]=index
                    
            elif a==0 and b ==n-1:
                a=1
                b = n-1
                index+=1
                square[a][b]=index
                
            elif a==0 and b<n-1:
                a = n-1
                b+=1
                index +=1
                square[a][b]=index
                
            elif a<n+1 and b==n-1:
                a-=1
                b =0
                index +=1
                square[a][b]=index
                

                
        return square
                
print(create_square(7)
