# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:33:23 2020

k-core-truss Decomposition algorithm

@author: Mariusz
"""
import os, sys
#FILEPATH = "fig2.txt"
#FILEPATH = "fig2.txt"
#FILEPATH = "fig3.txt"

#FILEPATH = "PPI.txt"
#FILEPATH = "random_100.txt"
#FILEPATH = "random_10000.txt"

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
    print ("Loaded graph has", len(graph_lines), "nodes")
    # For all lines get node and edges and put them to SET
    for line in graph_lines:
        line = line.rstrip('\n')
        neighbors = line.split(' ')
        #node = int(neighbors[0])
        node = neighbors[0]
        graph_dict[node] = set([])
        for neighbor in neighbors[1:]:
            #graph_dict[node].add(int(neighbor))
            graph_dict[node].add(neighbor)
    return graph_dict

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def node_degree(graph_dict, node):
    """
    Input: undirected graph, node
    Output: if node exist degree of the node in the graph
    """
    degree = 0
    if node in graph_dict:
        degree = len(graph_dict[node])

    return degree

def graph_degree(graph_dict):
    """
    Input: undirected graph
    Output: dictionary with node degrees
    """
    degree_dict = {}
    
    for item in graph_dict:
        degree_dict[item] = len(graph_dict[item])
        
    return degree_dict

def graph_edges(graph_dict):
    """
    Input: undirected graph
    Output: set of edge pairs in tuples
    """
    edges = set([])
    for item in graph_dict:
        nodes = graph_dict[item]
        for element in nodes:
            # check to avoid duplicates
            if (element,item) not in edges:
                edges.add((item, element))
    
    return edges

def common_nodes(graph_dict, node_v, node_u):
    """
    Input: undirected graph, node v and u
    Outpu: return tuple with common nodes
    """
    common_nodes = []
    
    for element in graph_dict[node_v]:
        if element in graph_dict[node_u]:
            common_nodes.append(element)
          
    return tuple(common_nodes)
    
def edge_degree(graph_degree, graph_edge):
    """
    Input: edge dictionary and graph
    Ouput: edge degree dictionary    
    """
    degree_edge_dict = {}
    for edge in graph_edge:
        # Make sure that node exist in the graph degree 
        if edge[0] in graph_degree and edge[1] in graph_degree:
            degree_edge_dict[edge] = min(graph_degree[edge[0]],graph_degree[edge[1]])
        else:
            print ("\nGraph is directed! - Closing Program")
            sys.exit()
    
    return degree_edge_dict

def edge_support(graph_dict, graph_edge):
    """
    Input: graph edges dictionary
    Output: edge support dictionary
    """
    support_edge_dict = {}
    for edge in graph_edge:   
        support_edge_dict[edge] = common_nodes(graph_dict, edge[0], edge[1])
    
    return support_edge_dict

def edge_support_num(graph_dict, graph_edge):
    """
    Input: graph edges dictionary
    Output: edge support dictionary with numbers
    """
    support_edge_dict = {}
    for edge in graph_edge:   
        support_edge_dict[edge] = len(common_nodes(graph_dict, edge[0], edge[1]))
    
    return support_edge_dict

def check(edges, nodeDegree, supHnum, vark, alpha):
    
    for edge in edges:
        if min(nodeDegree[edge[0]], nodeDegree[edge[1]]) <= vark/alpha:
            if supHnum[edge] <= vark - 2:
                return edge            
    return ()

def update_graph(edge, graph, edges):
    """
    Input: edge to be removed, undirected graph and edge set
    Output: None, It will mutate input objects
    """

    if edge in edges:
        edges.remove(edge)

    if edge[1] in graph[edge[0]]:
        graph[edge[0]].remove(edge[1])
    if edge[0] in graph[edge[1]]:
        graph[edge[1]].remove(edge[0])
    
    # Remove node if it is not connected
    if len(graph[edge[0]]) == 0:
        graph.pop(edge[0])
    
    if len(graph[edge[1]]) == 0:
        graph.pop(edge[1])
        
def remove_element(delitem, elements):
    """        
    Input: delitem, element in graph to be updated, graph in form of dictionary
    Output: return updated tuple
    """  
    elements_list = list(elements)
    if delitem in elements_list:
        elements_list.remove(delitem)

    return tuple(elements_list)
    
def kCrossTruss(graph_dict, alpha = 1):
    """
    Input: undirected graph and alpha by default 1
    Output: core-truss number for all edges in graph
    """
    # variable k - initial degree of vertices, nodes
    # algorithm assumption is that graph is connected
    # line 1
    vark = 2
    
    # graph H - initially full graph. Copy it in order not to mutate original 
    # line 1
    graphH = copy_graph(graph_dict)
    
    # Initialise dictionary with nodes degrees
    # line 2
    degreeH = graph_degree(graph_dict)  

    # Initialise list with edges of the graph H
    graphE = graph_edges(graphH)
    
    # line 3, 4
    # Initialise edge dictionary, degH(e)
    degreeEdgeH = edge_degree(degreeH, graphE)
    
    # line 5, 6
    # initialise support edge dictionary supH(e)   
    supH = edge_support(graphH, graphE)
    
    # inititalise support edge dictionary with degrees. Can be used but
    # in this implementation just edge dictionary is used
    supHnum = edge_support_num(graphH, graphE)  
   
    # initialise k-core-truss dictionary
    ctk = {}
    
    # line 7 - 19
    # while edges exist in EH
    # line 17 - 19
    while len(graphE) > 0:
        # while edge(u,v) exists such that edge degree is <= k/alpha and 
        # support edge dictionary <= k - 2
        # line 7
        ctkEdge = check(graphE, degreeH, supHnum, vark, alpha)

        while len(ctkEdge) > 0:
        #while vark == 2:    
            # reduce degree of node u
            # line 8
            degreeH[ctkEdge[0]] -= 1
            # reduce degree of node v
            # line 9
            degreeH[ctkEdge[1]] -= 1

            # reduce degrees for support degree and 
            # line 10
            elements = supH[ctkEdge]
                
            for element in elements:

                # Removing edge, equivalent or reducing degree by 1
                # line 11
                # check in case edge is defined other way round
                if (ctkEdge[0],element) in supHnum:
                    supHnum[(ctkEdge[0],element)] -= 1
                
                if (element, ctkEdge[0]) in supHnum:
                    supHnum[(element, ctkEdge[0])] -= 1

                # Removing edge, equivalent or reducing degree by 1
                # line 12
                if (ctkEdge[1],element) in supHnum:
                    supHnum[(ctkEdge[1],element)] -= 1

                if (element,ctkEdge[1]) in supHnum:
                    supHnum[(element,ctkEdge[1])] -= 1
            
                # Update edge degree of (u,w)
                # line 13
                degreeEdgeH[(ctkEdge[0],element)] = min(degreeH[ctkEdge[0]],degreeH[element])
            
                # Update edge degree of (v,w)
                # line 14
                degreeEdgeH[(ctkEdge[1],element)] = min(degreeH[ctkEdge[1]],degreeH[element])
                    
            # line 15 add edge to dictionary and assign current 
            ctk[ctkEdge] = vark
        
            # Remove nodes from graphH and edge from graphE . Mutate graphH and graphE 
            # line 16
            update_graph(ctkEdge, graphH, graphE)
            
            # check if there are any edges to meet the condition
            # related to line 7
            ctkEdge = check(graphE, degreeH, supHnum, vark, alpha)
        
        # increment variable k - to see if there areany higher core-truss subgraphs
        # line 18
        vark += 1    
                    
    return ctk, vark

if __name__ == "__main__":
    #graph_dict = load_graph(FILEPATH)
    print ("Enter path to node configuration file:")
    filename = input()
    #filename = FILEPATH
    if os.path.exists(filename):
        graph_dict = load_graph(filename)
        #print (graph_dict)
        kcrosstruss = kCrossTruss(graph_dict)
        print (kcrosstruss[0])
        print ("\nHighest K-Core-Truss:", kcrosstruss[1] - 1)
    else:
        print("Check path or file name!")

