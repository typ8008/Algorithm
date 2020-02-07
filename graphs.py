# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:25:52 2020

@author: NowakM
"""

import matplotlib.pyplot as plt
from random import seed
from random import random, choice


FILEPATH = "c:/Private/Algorithm/alg_phys-cite.txt"

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

class DPATrial:
    """
    Optimised trials for DPA algorithm
    Uses random.choice() to select a node number from this list for each trial
    """
    def __init__(self,num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """       
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range (num_nodes) for dummy_idx in range(num_nodes)]
        #print self._node_numbers

    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors    

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


def in_degree_normalized(digraph):
    """
    Takes directional graph as dictionary and
    returns normalised disribution of in-degree nodes
    """
    # get unnormalised graph
    unnormalized_graph = in_degree_distribution(digraph)
    
    # get number of nodes in the graph   
    num_nodes = len(digraph)
    
    # intialise normalized dictionary
    normalized_dict = {}
    
    # calculate normalized dictionary
    for node in unnormalized_graph:
        normalized_dict[node] = unnormalized_graph[node] / float(num_nodes)
    
    return normalized_dict


def random_ER_graph(num_nodes,probability):
    """
    Function takes number of nodes and probability
    returns graph as dictionary
    """    

    graph_dict = {}
    seed(1)
    
    for node_i in range(num_nodes):
        graph_dict[node_i] = set([])
        for node_j in range(num_nodes):
            a_rand = random()
            if a_rand < probability:
                if node_i != node_j:
                    graph_dict[node_i].add(node_j)

    return graph_dict

def random_DPA_graph(num_nodes,m_nodes):
    """ 
    Takes total number of nodes and number of nodes new node will be connected to
    return graph as a dictionary
    """
    graph_dict = make_complete_graph(m_nodes)
    
    trial = DPATrial(m_nodes)
        
    for node in range(m_nodes, num_nodes):
        graph_dict[node] = trial.run_trial(m_nodes)
    
    return graph_dict

def average_out_degree(digraph):
    """
    Takes a directional graph as a Dictionary and 
    returns average number of out degree
    """
    average  = 0
    
    for node in digraph:
        average += len(digraph[node])
    
    print "Num Edges", average
    average = float(average)/len(digraph)
    
    return average
    


def load_graph(path):
    """"
    Function takes file path and returns graph definition as Dictionary
    """
    
    # initialise dictionary
    graph_dict = {}
    
    # open File for reading
    graph_file = open(path,'r')
    
    # initialise list of all the lines
    graph_lines = graph_file.readlines()   
    print "Loaded graph has", len(graph_lines), "nodes"
    # For all lines get node and edges and put them to SET
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        graph_dict[node] = set([])
        for neighbor in neighbors[1:-1]:
            graph_dict[node].add(int(neighbor))
            
    return graph_dict
    

def graph_plot(graph_dict):
    
    idx = []
    val_y = []
    for key in graph_dict:
        idx.append(key)
        val_y.append(graph_dict[key])
    
    plt.plot(idx,val_y,'bo')
    #plt.xscale("log")
    #plt.yscale("log")
    #plt.title("Log/Log plot of in_degree distribution")
    plt.title("Log/Log plot of in_degree distribution DPA")
    plt.ylabel("Number of nodes")
    plt.xlabel("in-degree of nodes")
    #plt.figure(figsize=[10.0,10.0],dpi=600,frameon=True)
    #plt.draw()
    plt.show()
    
    
graph_dict = load_graph(FILEPATH)      

dpa = random_DPA_graph(28000,13)

normalised = in_degree_normalized(dpa)
graph_plot(normalised)

#normalised = in_degree_normalized(graph_dict)

#graph_plot(normalised)

#er_graph = random_ER_graph(len(graph_dict),0.05)

#er_graph = random_ER_graph(10000,0.0005)
#print er_graph
#normalised = in_degree_normalized(er_graph)

#graph_plot(normalised)

#print average_out_degree(graph_dict)


#x = range(6)
#y = []

#for idx in x:
#    y.append(idx**2)

