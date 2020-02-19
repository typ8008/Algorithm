# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:47:30 2020

@author: NowakM
"""

from collections import deque

GRAPH0 = {0: set([1]),
          1: set([0, 2]),
          2: set([1, 3]),
          3: set([2])}

GRAPH1 = {0: set([1, 2, 3, 4]),
          1: set([0, 2, 3, 4]),
          2: set([0, 1, 3, 4]),
          3: set([0, 1, 2, 4]),
          4: set([0, 1, 2, 3])}


GRAPH5 = {"dog": set(["cat"]),
          "cat": set(["dog"]),
          "monkey": set(["banana"]),
          "banana": set(["monkey", "ape"]),
          "ape": set(["banana"])}


def bfs_visited(upgraph, start_node):
    """
    Takes undirected graph and start node and 
    returns set consisting of all nodes that are visited by breath-first search
    """
    visited = set([])
    queue = deque()
    visited.add(start_node)
    queue.append(start_node)
    
    while len(queue) > 0:
        node = queue.pop()

        for neighbor in upgraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited

def cc_visited(ugraph):
    """
    Takes undirected graph and 
    returns list of sets, where each set consists of all the nodes in a connected
    components
    """
    remaining_nodes = [node for node in ugraph]
    connected_components = []
    
    while len(remaining_nodes) > 0:
        node = remaining_nodes[0]
        set_w = bfs_visited(ugraph,node)
        if set_w not in connected_components:
            connected_components.append(set_w)
        remaining_nodes.pop(0)
    
    return connected_components

def largest_cc_size(ugraph):
    """
    Takes undirected graph and
    returns integer of largest connected set
    """
    cc_list = cc_visited(ugraph)
    largest = 0
    for item in cc_list:
        if len(item) > largest:
            largest = len(item)
    
    return largest

def compute_resilience(ugraph,attack_order):
    """
    Takes undirected graph and list of nodes and 
    returns list of largest connected components
    """
    lcc_list = []
    
    lcc_list.append(largest_cc_size(ugraph))
    print lcc_list
    for node in attack_order:
        node_set = ugraph.pop(node)
        edge_list = list(node_set)
        for edge in edge_list:
            temp_set = ugraph.pop(edge)
            temp_set.discard(node)
            ugraph[edge] = temp_set

        lcc_list.append(largest_cc_size(ugraph))
    
    return lcc_list

#print bfs_visited(GRAPH5,"monkey")
#print cc_visited(GRAPH5)
#print largest_cc_size(GRAPH0)
print compute_resilience(GRAPH0,[1,2])