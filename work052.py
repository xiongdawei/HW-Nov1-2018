#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:07:58 2018

@author: davidxiong
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:48:05 2018

@author: davidxiong
"""
import random
import numpy as np
def test1(k,p):
    while k>1:
        k-=1
        p = p*k
        return p


class judge():
    def _init_(self,matrix):
        self.matrix = matrix
   
    def row(self,matrix):
        return sum(matrix[0])
 
    def col(self,matrix):
        s = 0
        for i in range(len(matrix)):
            s = s + matrix[0][i]
        return s
        
    def diagonal_left(self,matrix):
        S = 0
        for i in range(len(matrix)):
            S = S + matrix[i][i]
        return S
    
    def diagonal_right(self,matrix):
        S = 0
        for i in range(matrix):
            S = S + matrix[i][len(matrix)-i]
        return S
    
    def magic_sqaure(self,matrix):
        a = judge()
        
        if a.row(matrix) == a.col(matrix) == a.diagonal_left(matrix) == a.diagonal_right(matrix):
            return "It is"
        else:
            return "It isn't"
            
            
         
a = [[1,4],[2,3]]
obj = judge()
print(obj.magic_sqaure(a))


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            