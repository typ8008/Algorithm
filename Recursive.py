# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:20:53 2020

@author: Mariusz
"""
def Recursive(A):
    # check if there is only one item left. If so, return it 
    if len(A) == 1:
         return A[0]

    # take the left item and recurse on the list if the opponent 
    # were to take the left side, and the list if the opponent 
    # were to take the right number
    takeLeftSide = A[0] + max(Recursive(A[1:-1]), Recursive(A[2:len(A)]))
    takeRightSide = A[-1] + max(Recursive(A[0:-2]), Recursive(A[1:-1]))

    return max(takeLeftSide, takeRightSide)

if __name__ == '__main__':
    A = [5,8,1,3,6]
    print Recursive(A)
    
    
