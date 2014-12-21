# -*- coding: utf-8 -*-
#Python Problem 2
#hamming.py
#Introduction to Bioinformatics Assignment 2
#Purpose: To utilize nested for loops, intro to alignments, if statements.
#Your Name: Diane Kaplan
#Date: October 4, 2014

#stores 3 database sequences
seqList = ["AGGATACAGCGGCTTCTGCGCGACAAATAAGAGCTCCTTGTAAAGCGCCAAAAAAAGCCTCTCGGTCTGTGGCAGCAGCGTTGGCCCGGCCCCGGGAGCGGAGAGCGAGGGGAGGCAGATTCGGAGGAAGGTCTGAAAAG",
           "AAAATACAGGGGGTTCTGCGCGACTTATGGGAGCTCCTTGTGCGGCGCCATTTTAAGCCTCACAGACTATGGCAGCAGCGTTGGCCCGGCAAAAGGAGCGGAGAGCGAGGGGAGGCGGAGACGGACGAAGGTCTGAGCAG",
           "CCCATACAGCCGCTCCTCCGCGACTTATAAGAGCTCCTTGTGCGGCGCCATTTTAAGCCTCTCGGTCTGTGGCAGCAGCGTTGGCCCGCCCAAAACAGCGGAGAGCGAGGGGAGGCGGAGACGGAGGAAGGTCTGAGCAG"]

#your query sequence
s1 = "AGGATACAGCGGCTTCTGCGCGACTTATAAGAGCTCCTTGTGCGGCGCCATTTTAAGCCTCTCGGTCTGTGGCAGCAGCGTTGGCCCGGCCCCGGGAGCGGAGAGCGAGGGGAGGCGGAGACGGAGGAAGGTCTGAGGAG"

#hamming_distance finds the number of differences between two sequences:
#compare values for inequality at each position in the sequence and increment counter
def hamming_distance (seq, comparison_seq):  
    cursor = 0
    string_length = len(seq)
    difference_counter = 0

    while cursor < string_length:  #ours are all the same length, could also add a check/flexbility
        if seq[cursor] != comparison_seq[cursor]:        
    	   difference_counter += 1
        cursor += 1
    return difference_counter

#list_compare takes a sequence and a list of comparison strings and gives you the winning match 
#Future note: could add support for tie scores
def list_compare (seq, list):  
    best_score = 0  
    best_seq = ''
    for string in list:
        score =  hamming_distance(seq, string )
        if score > best_score:
            best_score = score
            best_seq = string
    return best_score, best_seq

#results
for string in seqList:
    print "The Hamming distance vs comparison string = ",  hamming_distance(s1, string )
print "\r"
print "Comparing a sequence with a list of many, the winning score and sequence was:" , list_compare(s1, seqList)


