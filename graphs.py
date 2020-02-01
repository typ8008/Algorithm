# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:25:52 2020

@author: NowakM
"""

EX_GRAPH0 = {0: set([1,2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3,7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}

GRAPH0 = {0: set([1]),
          1: set([2]),
          2: set([3]),
          3: set([0])}


GRAPH1 = {0: set([]),
          1: set([0]),
          2: set([0]),
          3: set([0]),
          4: set([0])}

GRAPH4 = {"dog": set(["cat"]),
          "cat": set(["dog"]),
          "monkey": set(["banana"]),
          "banana": set([])}

def make_complete_graph(num_nodes):
    """
    Take number of nodes and returns dictionary representing graph 
    with all possible edges without selfloop
    """
    # if number of nodes is positive number
    if num_nodes > 0:
         # Define empty dictionary
        graph = {}
        for node in range(num_nodes):
            node_list = range(num_nodes)
            node_list.remove(node)
            graph[node] = set(node_list)
        return graph
    
    return {}

def compute_in_degrees(digraph):
    """
    Takes directed graph as dictionary and
    returns dictionary of the in-degree of the nodes
    """
    # create degree dictionary
    degree_dict = {}
    
    # create all nodes list
    all_nodes = []
    
    # create combine list of all the input nodes and 
    for node in digraph:
        degree_dict[node] = 0
        all_nodes.extend(list(digraph[node]))
    
    for node in digraph:
        degree_dict[node] = all_nodes.count(node)
        
    return degree_dict

def in_degree_distribution(digraph):
    """
    Takes directional graph as dictionary and 
    returns unnormalised distribution of in-degree of the nodes
    """
    # create iterator of lenght of nodes
    # create empty node list
    node_list = []    
    
    # all nodes
    all_items = []

    # create empty degree list
    degree_list = [0 for dummy_item in range(len(digraph))]

    # populate node list and initiliaze degree list
    for value in digraph:
        node_list.append(value)
        all_items.extend(list(digraph[value]))
    
    # sort the node list    
    node_list.sort()
    
    # populate degree list
    for node in node_list:
        occurance = all_items.count(node)    
        degree_list[occurance] += 1    
    
    # create degree dictionalry
    degree_dict = {}
    
    # populate degree dictionary
    for degree in range(len(degree_list)):
        if degree_list[degree] > 0:
            degree_dict[degree] = degree_list[degree]
        
    return degree_dict