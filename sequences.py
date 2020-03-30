# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:20:03 2020

@author: Mariusz
"""

"""
Provide code and solution for Application 4
"""

DESKTOP = True

import math
import random
import urllib2

if DESKTOP:
    import matplotlib.pyplot as plt
    #import alg_project4_solution as student
else:
    import simpleplot
    import userXX_XXXXXXX as student
    

# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"

###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.  

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict

def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq

def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)
    
    # read in files as string
    words = word_file.read()
    
    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list

def build_scoring_matrix(alphabet,diag_score,off_diag_score,dash_score):
    """
    Input: Set of characters - alphabet, diag_score, off_diag_score, dash_score
    Output: Returns dictionary of dictionaries index by pairs of characters plus "-"
    """
    #alphabet.add("-")
    alphabet_copy = alphabet.copy()
    alphabet_copy.add("-")
    matrix_dict = {}
    score = 0
    for char_x in alphabet_copy:
        score_matrix = {}
        for char_y in alphabet_copy:
            if char_x == "-" or char_y == "-":
                score = dash_score
            elif char_x == char_y: 
                score = diag_score
            else:
                score = off_diag_score                
            score_matrix[char_y] = score
        #score_matrix["-"] = dash_score    
        matrix_dict[char_x] = score_matrix    
    
    return matrix_dict
 
def compute_alignment_matrix(seq_x,seq_y,scoring_matrix,global_flag):   
    """
    Input: 2 sequences, X, Y and scoring matrix, global_flag = True - global, False - Loca
    Output: Computes and returns alignment matrix
    """
    
    var_m = len(seq_x)
    var_n = len(seq_y)
    
    matrix_s = [[0 for dummy_col in range(var_n + 1)] for dummy_row in range(var_m + 1)]
    
    for idx in range(1,var_m+1):
        matrix_s[idx][0] = matrix_s[idx-1][0] + scoring_matrix[seq_x[idx-1]]["-"]
        if global_flag == False and matrix_s[idx][0] < 0:
            matrix_s[idx][0] = 0
            
    for idy in range(1,var_n+1):
        matrix_s[0][idy] = matrix_s[0][idy-1] + scoring_matrix["-"][seq_y[idy-1]]
        if global_flag == False and matrix_s[0][idy] < 0:
            matrix_s[0][idy] = 0

    for idi in range(1,var_m+1):
        for idj in range(1,var_n+1):
            matrix_s[idi][idj] = max(matrix_s[idi - 1][idj -1] + scoring_matrix[seq_x[idi-1]][seq_y[idj-1]],\
                    matrix_s[idi-1][idj] + scoring_matrix[seq_x[idi-1]]["-"],\
                    matrix_s[idi][idj-1] + scoring_matrix["-"][seq_y[idj-1]])
            if global_flag == False and matrix_s[idi][idj] < 0:
                matrix_s[idi][idj] = 0
    return matrix_s
 
def compute_global_alignment(seq_x,seq_y,scoring_matrix,alignment_matrix):
    """
    Input: 2 Sequences X, Y, scoring matrix and alignment matrix
    Output: Computes global alignment score and returns tuple (score, align_x, align_y), 
    align x and y have the same lenght
    """
    score = 0
    align_x = ""
    align_y = ""
    var_i = len(seq_x)
    var_j = len(seq_y)
    
    while var_i != 0 and var_j != 0:
        if alignment_matrix[var_i][ var_j] == \
        alignment_matrix[var_i - 1][var_j -1] + \
        scoring_matrix[seq_x[var_i-1]][seq_y[var_j-1]]:
            align_x = seq_x[var_i - 1] + align_x
            align_y = seq_y[var_j - 1] + align_y
            var_i -= 1
            var_j -= 1
        else:
            if alignment_matrix[var_i][var_j] == \
             alignment_matrix[var_i - 1][var_j] + \
             scoring_matrix[seq_x[var_i-1]]["-"]:
                 align_x = seq_x[var_i - 1] + align_x
                 align_y = "-" + align_y
                 var_i -= 1
            else:
                align_x = "-" + align_x
                align_y = seq_y[var_j - 1] + align_y
                var_j -= 1
    
    while var_i != 0:
        align_x = seq_x[var_i - 1] + align_x
        align_y = "-" + align_y
        var_i -= 1
    while var_j != 0:
        align_x = "-" + align_x
        align_y =  seq_y[var_j - 1] + align_y
        var_j -= 1          
    
    # calculate score of the alignment
    for index in range(len(align_x)):
        score += scoring_matrix[align_x[index]][align_y[index]] 
    
    return (score,align_x, align_y)
    
def compute_local_alignment(seq_x,seq_y,scoring_matrix,alignment_matrix):
    """
    Input: 2 sequence X and Y, scoring matrix and alignment matrix
    Output: Computes Local Alignment and returns tuple (score, align_x, align_y)
    """
    score = 0
    align_x = ""
    align_y = ""
    var_i = len(seq_x)
    var_j = len(seq_y)
    maximum = [float('-inf'),0,0]
    # Find maximum value
    for idx in range(len(alignment_matrix)):
        for idy in range(len(alignment_matrix[idx])):
            if alignment_matrix[idx][idy] > maximum[0]:
                maximum = [alignment_matrix[idx][idy],idx,idy]
    
    #print maximum
    
    var_i = maximum[1]
    var_j = maximum[2]
    
    while var_i != 0 and var_j != 0 and alignment_matrix[var_i][var_j] != 0:
        if alignment_matrix[var_i][ var_j] == \
        alignment_matrix[var_i - 1][var_j -1] + \
        scoring_matrix[seq_x[var_i-1]][seq_y[var_j-1]]:
            align_x = seq_x[var_i - 1] + align_x
            align_y = seq_y[var_j - 1] + align_y
            var_i -= 1
            var_j -= 1
        else:
            if alignment_matrix[var_i][var_j] == \
             alignment_matrix[var_i - 1][var_j] + \
             scoring_matrix[seq_x[var_i-1]]["-"]:
                 align_x = seq_x[var_i - 1] + align_x
                 align_y = "-" + align_y
                 var_i -= 1
            else:
                align_x = "-" + align_x
                align_y = seq_y[var_j - 1] + align_y
                var_j -= 1
    
    #while var_i != 0:
    #    align_x = seq_x[var_i - 1] + align_x
    #    align_y = "-" + align_y
    #    var_i -= 1
    #while var_j != 0:
    #    align_x = "-" + align_x
    #    align_y =  seq_y[var_j - 1] + align_y
    #    var_j -= 1          
    
    # calculate score of the alignment
    for index in range(len(align_x)):
        score += scoring_matrix[align_x[index]][align_y[index]] 
    
    return (score,align_x, align_y)   
    
#scoring = build_scoring_matrix(set(['A', 'C', 'T', 'G']), 6, 2, -4)
#print "Scoring Matrix", scoring
#scoring = {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}
#alignment = compute_alignment_matrix('A', 'AC',scoring , True)

#print compute_global_alignment('A','AC',scoring,alignment)
#print compute_local_alignment('A','AC',scoring,alignment)
 
human_seq = read_protein(HUMAN_EYELESS_URL)
fly_seq = read_protein(FRUITFLY_EYELESS_URL)    
concensus_seq  = read_protein(CONSENSUS_PAX_URL)

# Question 1
scoring_matrix = read_scoring_matrix(PAM50_URL)
human_fly_alignment = compute_alignment_matrix(human_seq, fly_seq, scoring_matrix, False)
#print "alignmnent", human_fly_alignment
local_alignment = compute_local_alignment(human_seq, fly_seq, scoring_matrix,human_fly_alignment)

# Question 2
human_aligned_seq = local_alignment[1].replace("-","")
fly_aligned_seq = local_alignment[2].replace("-","")

human_consensus_matrix = compute_alignment_matrix(human_aligned_seq,concensus_seq,scoring_matrix,True)
fly_consensus_matrix = compute_alignment_matrix(fly_aligned_seq,concensus_seq,scoring_matrix,True)

human_concensus_align = compute_global_alignment(human_aligned_seq,concensus_seq,scoring_matrix,human_consensus_matrix)
fly_concensus_align = compute_global_alignment(fly_aligned_seq,concensus_seq,scoring_matrix,fly_consensus_matrix)

#print len(human_concensus_align[1]), len(human_concensus_align[2])


total = 0
for idx in range(len(human_concensus_align[1])):
    if human_concensus_align[1][idx] == human_concensus_align[2][idx]:
        total +=1

print "human percentage", total*100.0/(len(human_concensus_align[1]))

total = 0
for idx in range(len(fly_concensus_align[1])):
    if fly_concensus_align[1][idx] == fly_concensus_align[2][idx]:
        total +=1

print "fly percentage", total*100.0/len(fly_concensus_align[1])

#Question 3

human_random = ""
for idx in range(len(human_concensus_align[1])):
    human_random += random.choice("ACBEDGFIHKMLNQPSRTWVYXZ")

fly_random = ""
for idx in range(len(fly_concensus_align[1])):
    fly_random += random.choice("ACBEDGFIHKMLNQPSRTWVYXZ")


total = 0
for idx in range(len(human_concensus_align[1])):
    if fly_random[idx] == human_random[idx]:
        total +=1

print "human percentage", total*100.0/(len(human_concensus_align[1]))

total = 0
for idx in range(len(fly_concensus_align[1])):
    if fly_concensus_align[1][idx] == fly_random[idx]:
        total +=1

print "fly percentage", total*100.0/len(fly_concensus_align[1])

#Question 4

def generate_null_distribution(seq_x,seq_y,scoring_matrix,num_trials):
    """
    Input: Takes 2 sequences, scoring matrix and number of trials
    Output: Computes and returns un-normalised Scoring Distribution
    """
    scoring_distribution = {}
    for num in range(num_trials):
        
        char_list = list(seq_y) # convert string into list
        random.shuffle(char_list) #shuffle the list
        rand_y = ''.join(char_list)
    
        align_matrix = compute_alignment_matrix(seq_x,rand_y,scoring_matrix, False)
        local_align =  compute_local_alignment(seq_x, rand_y,scoring_matrix,align_matrix)
    
        score = local_align[0]
        #print "score", score
        
        if score in scoring_distribution.keys():
            scoring_distribution[score] += 1
        else:
            scoring_distribution[score] = 1
    
    print scoring_distribution
    for element in scoring_distribution:
        print element
        scoring_distribution[element] = scoring_distribution[element]/float(num_trials)
    
    graph_plot(scoring_distribution)
    
    return scoring_distribution
    #if scoring_distribut

def graph_plot(graph_dict):
    
    idx = range(101)
    val_y = []
   
    
    for key in idx:
        if key in graph_dict.keys():  
            val_y.append(graph_dict[key])
        else:
            val_y.append(0)
            
        
    plt.bar(idx,val_y)

    
    #plt.xscale("log")
    #plt.yscale("log")
    #plt.title("Log/Log plot of in_degree distribution")
    plt.title("Null Distribution for Testing Random Shuffle Seq over 1000 Trials")
    plt.ylabel("Fractions of trials")
    plt.xlabel("Scores")
    #plt.legend(loc="upper right")
    #plt.grid()
    #plt.figure(figsize=[10.0,10.0],dpi=600,frameon=True)
    #plt.draw()
    plt.show()

#print generate_null_distribution(human_seq,fly_seq,scoring_matrix,1000)

# Question 5
null_dist_dict = {39: 4, 40: 5, 41: 14, 42: 22, 43: 31, 44: 47, 45: 47, 46: 59, 47: 74, 48: 66, 49: 76, 50: 60, 51: 66, 52: 53, 53: 44, 54: 37, 55: 44, 56: 45, 57: 24, 58: 33, 59: 20, 60: 20, 61: 19, 62: 14, 63: 13, 64: 10, 65: 7, 66: 6, 67: 7, 68: 9, 69: 2, 70: 4, 71: 2, 72: 5, 73: 2, 74: 3, 75: 1, 79: 1, 81: 1, 82: 1, 87: 2}
null_dist_dict_normalised = {39: 0.004, 40: 0.005, 41: 0.014, 42: 0.022, 43: 0.031, 44: 0.047, 45: 0.047, 46: 0.059, 47: 0.074, 48: 0.066, 49: 0.076, 50: 0.06, 51: 0.066, 52: 0.053, 53: 0.044, 54: 0.037, 55: 0.044, 56: 0.045, 57: 0.024, 58: 0.033, 59: 0.02, 60: 0.02, 61: 0.019, 62: 0.014, 63: 0.013, 64: 0.01, 65: 0.007, 66: 0.006, 67: 0.007, 68: 0.009, 69: 0.002, 70: 0.004, 71: 0.002, 72: 0.005, 73: 0.002, 74: 0.003, 75: 0.001, 79: 0.001, 81: 0.001, 82: 0.001, 87: 0.002}

total = 0
for item in null_dist_dict:
    total += item * null_dist_dict[item]
    
mean = total/1000.0
print "mean", mean

total = 0

for item in null_dist_dict:
    total += ((item - mean)**2)* null_dist_dict[item]
                
std = (total/1000.0)**0.5

print "standard deviation", std

print "z", (875 - mean)/std

#Question 7
word_score_matrix = build_scoring_matrix(set(list("ACBEDGFIHKMLNQPSRTWVYXZ")),2,1,0)
print word_score_matrix

word1 = "KITTEN"
word2= "SITTING"
word_global_matrix = compute_alignment_matrix(word1, word2 , word_score_matrix, True)
word_global_align = compute_global_alignment(word1,word2,word_score_matrix,word_global_matrix)

#print word_global_align, len(word1), len(word2)
print "Edit Distance", len(word1) + len(word2) - word_global_align[0]

#Question 8
word_list = read_words(WORD_LIST_URL)

def check_spelling(checked_word, dist, word_list):
    """
    Input: Takes word to check, edit distance and word list
    Output: Iterates trough all the words and returns all words within edit distance from given word
    """
    word_score_matrix = build_scoring_matrix(set(list("abcdefghijklmnoprstuvqwxyz")),2,1,0)
    match_list = []
    for word in word_list:
        word_global_matrix = compute_alignment_matrix(checked_word, word , word_score_matrix, True)    
        word_global_align = compute_global_alignment(checked_word, word, word_score_matrix, word_global_matrix)
        if len(checked_word)+len(word) - word_global_align[0] <= dist:
            match_list.append(word)
            
    return match_list

print "humble", check_spelling("humble", 1, word_list)
print "firefly", check_spelling("firefly", 2, word_list)
        