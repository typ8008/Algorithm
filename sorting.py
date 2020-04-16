# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:45:56 2020
This program with compare insertion sort and selection sort algorithms

@author: Mariusz
"""
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

def min_element(input_list):
    """
    Input: takes a list of element
    Output: returns list with [min element, index in list]
    """
    
    element = [float('inf'), 0]
    for idx in range(len(input_list)):
        if element[0] > input_list[idx]:
            element = [input_list[idx], idx]
            
    return element

def selection_sort(input_list):
    """
    Input: list of elements
    Output: sorted list in incrementing way
    Sorted is done in place starting from current element and comparing against 
    onwards once. If there is a smaller element in the sublist then it's swapped
    with current element
    """
    # create a copy not to modify original list
    
    list_copy = input_list.copy()
    
    for idx in range(len(list_copy)):        
        min_el = min_element(list_copy[idx + 1:])
        if list_copy[idx] > min_el[0]:
            list_copy[idx + min_el[1] + 1] = list_copy[idx]
            list_copy[idx] = min_el[0]                
    
    return list_copy

def insertion_sort(input_list):
    """
    Input: list of elements
    Output: sorted list in incrementing way

    """
    # create a copy not to modify original list    
    list_copy = input_list.copy()
    
    for idx in range(1,len(list_copy)):
        item = list_copy[idx]
        idy = idx - 1
        while idy >= 0 and list_copy[idy] > item:
            list_copy[idy+1] = list_copy[idy]
            idy -= 1
        list_copy[idy+1] = item
    
    return list_copy

def reverse_list(num_elements):
    """
    Input: takes number of elements
    Output: list with reversed ordered of elements
    """
    elements_list = list(range(num_elements))
    elements_list.reverse()
    return elements_list


def random_list(num_elements):
    """
    Input: takes number of elements
    Output: list with randomly ordered elements
    """
    elements_list = list(range(num_elements))
    random.shuffle(elements_list)
    return elements_list

def running_time(max_num):
    """
    Input: Maximum Number of elements
    Output: Lists with running time for selection sort and insertion sort
    Function iterates from 1 to max_num - 1 and measure time of the execution
    """
    sel_list = []
    ins_list = [] 
    
    for num in range(max_num):
        #unsorted_list = random_list(num)
        unsorted_list = reverse_list(num)

        start = timer()
        selection_sort(unsorted_list)
        stop = timer()
        sel_list.append(stop - start)
     
        start = timer()
        insertion_sort(unsorted_list)
        stop = timer()
        ins_list.append(stop - start)

        
    return (sel_list, ins_list)

def graph_plot(sel_list, ins_list):
    """
    Input: List of running times for selection sort and insertion sort
    Output: Return None.
    Function will plot runninging time versur size of input
    """
    
    if len(sel_list) != len(ins_list):
        print ("Make sure lists are the same lenght")
        return
    
    idx = range(len(sel_list))
            
    plt.plot(idx,sel_list,'b', label='selection sort')
    plt.plot(idx,ins_list,'r', label='insertion sort')    

    plt.title("Selection Sort vs Insertion Sort")
    plt.ylabel("Running time [s]")
    plt.xlabel("Number of Nodes")
    plt.legend(loc="upper right")
    plt.grid()
    plt.show()


# Crete runtime list of algorithms
run_time = running_time(1000)
# Plot running time vs input size
graph_plot(run_time[0], run_time[1])

