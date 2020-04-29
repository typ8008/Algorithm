# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:25:49 2020

@author: Mariusz
"""


import random
from random import seed

def generate_undirected_graph():
    pass

def make_complete_graph(num_nodes):
    """
    Take number of nodes and returns dictionary representing graph 
    with all possible edges without self loop
    """
# if number of  is positive number
    if num_nodes > 0:
         # Define empty dictionary
         graph = {}
         for node in range(num_nodes):
             node_list = list(range(num_nodes))
             node_list.remove(node)             
             graph[node] = set(node_list)
    
         return graph
    return {}


def random_ER_graph(num_nodes,probability):
    """
    Function takes number of nodes and probability
    returns graph as dictionary
    """    

    graph_dict = {}
    seed(1)
    
    for node_i in range(num_nodes):
        if node_i not in graph_dict:
            graph_dict[node_i] = set([])
        for node_j in range(num_nodes):
            a_rand = random.random()
            if a_rand < probability:
                if node_i != node_j:
                    graph_dict[node_i].add(node_j)
                    
                    if node_j in graph_dict:
                        graph_dict[node_j].add(node_i)
                    else:
                        graph_dict[node_j] = set([node_i]) 

    return graph_dict


def save_to_file(dictionary, filename):
    """
    Input: dictionary and filename
    Output: None
    Takes dictionary representaion of a graph and saves it to the file
    """
    f = open(filename,'w+')
    for item in dictionary:
        string = str(item) + ' '
        for element in dictionary[item]:
            string += str(element) + ' '
        #string += '\n'
        string = string[:-1]
        print (string)
        f.write(string + '\n')
    f.close()
print (make_complete_graph(10))

#save_to_file(make_complete_graph(10000), 'full_10000.txt')
save_to_file(random_ER_graph(10000, 0.001), 'random_10000.txt')

#print (random_ER_graph(100, 0.1))
    