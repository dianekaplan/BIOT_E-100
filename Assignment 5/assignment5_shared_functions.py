# -*- coding: utf-8 -*-
#assignment5_functions.py
#Introduction to Bioinformatics
#Python Assignment 5
#Purpose: putting together the functions I'll use in the other programs
#Your Name: Diane Kaplan
#Date: December 5, 2014


#Function takes a sequence and returns the reverse complement
def reverseComplement(seq): 
    given_seq = seq
    seq_backward = seq[::-1] 
    base_partners = {"A":"T", "C":"G", "G":"C", "T":"A"} 
    reverse_complement = ""  

    #Loop through and look up the complement to create the new sequence
    for char in seq_backward:
        reverse_complement += base_partners[char]

    return reverse_complement

#Function takes a sequence and length N and returns a list of Nmers from that sequence
def make_Nmers_list(seq, n):
    thisSeq = seq
    seqLen = len(thisSeq)
    Nmer_list = []
    cursor = 0
    
    #loop through our sequence, saving Nmers to a list
    while cursor < seqLen-(n-1): 
        thisChunk = thisSeq[cursor:cursor+(n)]
        cursor += 1     
        Nmer_list.append(thisChunk)
        
    return Nmer_list   
