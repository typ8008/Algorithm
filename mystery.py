# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:49:12 2020

@author: Mariusz
"""

import itertools

def findsubsets(subset,num):
    return list(itertools.combinations(subset,num))


graph1 = {   1: set([]),
             2: set([3,7]),         
             3: set([2,4]),
             4: set([3,5]),
             5: set([4,6]),
             6: set([5,7]),
             7: set([2,6])}

graph2 = {   1: set([]),
             2: set([7]),         
             3: set([4]),
             4: set([3]),
             5: set([6]),
             6: set([5]),
             7: set([2])}

GRAPH3 = {0: set([4, 7, 10]), 1: set([5, 6]), 2: set([7, 11]), 3: set([10]), 4: set([0, 7, 11]), 5: set([1, 7]), 6: set([1]), 7: set([0, 2, 4, 5, 9, 11]), 8: set([9]), 9: set([7, 8]), 10: set([0, 3]), 11: set([2, 4, 7])}

GRAPH4 = {0: set([4, 7, 10, 12, 13]), 1: set([5, 6, 12]), 2: set([7, 11, 12, 14]), 3: set([10, 14, 15]), 4: set([0, 7, 11, 12, 13, 14]), 5: set([1, 7, 15]), 6: set([1, 13]), 7: set([0, 2, 4, 5, 9, 11, 14]), 8: set([9, 14, 15]), 9: set([7, 8]), 10: set([0, 3]), 11: set([2, 4, 7]), 12: set([0, 1, 2, 4]), 13: set([0, 4, 6, 15]), 14: set([2, 3, 4, 7, 8]), 15: set([3, 5, 8, 13])}

GRAPH5 = {0: set([4, 7, 10, 12, 13, 16]), 1: set([5, 6, 12]), 2: set([7, 11, 12, 14]), 3: set([10, 14, 15]), 4: set([0, 7, 11, 12, 13, 14, 17]), 5: set([1, 7, 15]), 6: set([1, 13]), 7: set([0, 2, 4, 5, 9, 11, 14, 18]), 8: set([9, 14, 15]), 9: set([7, 8, 19]), 10: set([0, 3]), 11: set([2, 4, 7]), 12: set([0, 1, 2, 4]), 13: set([0, 4, 6, 15, 16]), 14: set([2, 3, 4, 7, 8]), 15: set([3, 5, 8, 13]), 16: set([0, 13, 19]), 17: set([4]), 18: set([7]), 19: set([9, 16])}

GRAPH6 = {0: set([4, 7, 10, 12, 13, 16]), 1: set([5, 6, 12]), 2: set([7, 11, 12, 14]), 3: set([10, 14, 15]), 4: set([0, 7, 11, 12, 13, 14, 17]), 5: set([1, 7, 15]), 6: set([1, 13]), 7: set([0, 2, 4, 5, 9, 11, 14, 18]), 8: set([9, 14, 15]), 9: set([7, 8, 19]), 10: set([0, 3]), 11: set([2, 4, 7]), 12: set([0, 1, 2, 4]), 13: set([0, 4, 6, 15, 16]), 14: set([2, 3, 4, 7, 8]), 15: set([3, 5, 8, 13]), 16: set([0, 13, 17, 19]), 17: set([4, 16]), 18: set([7]), 19: set([9, 16])}

GRAPH1 = {1 : set([]), 2 : set([3, 7]), 3 : set([2, 4]), 4 : set([3, 5]), 5 : set([4, 6]), 6 : set([5, 7]), 7 : set([2, 6])}

GRAPH2 = {1 : set([2, 3, 4, 5, 6, 7]), 2 : set([1]), 3 : set([1]), 4 : set([1]), 5 : set([1]), 6 : set([1]), 7 : set([1])}

def mystery(ugraph):
    """
    Input: Undirected graph g=(V,E)
    Output: Subset that satisfies algorythm property
    """
    edges = []
    #nodes = list(ugraph)
    for node in ugraph:
        for edge in ugraph[node]:
            if (edge,node) not in edges:
                edges.append((node,edge))
    
    #edge = set((1,3))
    #subset = set((1,3,5,7))
    #print edges
    #print edge, subset, edge.intersection(subset)
     
    flag = False
    var_n = len(ugraph)
    #print var_n
    
    for var_i in range(var_n): 
        subsets = findsubsets(ugraph,var_i)        
        for subset in subsets:
            #print "subset", subset, subsets
            flag = True
            for edge in edges:
                
                if len(set(edge).intersection(set(subset))) == 0:
                #if set(edge).intersection(set(subset)) != set(edge):
                    flag = False
                    #print edge, subset
            if flag == True :               
                return subset
    

#print findsubsets(graph1,6)
print "return", mystery(graph1)
print "return", mystery(graph2)

print len(mystery(GRAPH1)) 
print len(mystery(GRAPH2))     # answer should be 6
print len(mystery(GRAPH3))    # answer should be 9
print len(mystery(GRAPH4))
print len(mystery(GRAPH5))
