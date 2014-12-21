# -*- coding: utf-8 -*-
#extinction.py
#Introduction to Bioinformatics
#Python Assignment 5, Problem 1
#Purpose: Calculate the extinction coefficient for a sequence using a given dictionary
#Your Name: Diane Kaplan
#Date: December 5, 2014

#Given a sequence, what's the extinction coefficient 
#What is the sequence of this molecule, 5’ to 3’?  
#Note: Assume that the molecule is all DNA, strip all modifications prior to submitting your answer. (1 point)

#  Start by storing your Mipomersen sequence as a string.
seq_to_test = "GCCTCAGTCTGCTTCGCACC" #this is 5' to 3'

#  Create a dictionary from the DNA part of Owczarzy’s table- DNA & its extinction coefficient
extinction_coefficient_dictionary = {"A":15400.0,"C":7400.0,"G":11500.0,"T":8700.0,"AA":27400.0,"AC":21200.0,"AG":25000.0,
"AT":22800.0,"CA":21200.0,"CC":14600.0,"CG":18000.0,"CT":15200.0,"GA":25200.0,"GC":17600.0,"GG":21600.0,"GT":20000.0,
"TA":23400.0,"TC":16200.0,"TG":19000.0,"TT":16800.0}

#extinctionCalc takes a sequence and a dictionary and returns the calculated extinction coefficient for the sequence
def extinctionCalc(seq, dictionary):
    thisSeq = seq
    seqLen = len(thisSeq)
    #thisSeq_antisense = reverseComplement(seq)  #this is 3' to 5'
    thisDictionary = dictionary
    calculated_extinction_coefficient = 0
    monomer_totals = 0
    dimer_totals = 0    
    
#loop through the sequence, looking up the value and adding it to the dimer_totals
    cursor = 0
    thisNucleotide= ''
    thisPair = ''
    this_extinction_value = 0
    
    #see where we are, add the values to totals, and move on
    while cursor < seqLen-1: 
        thisNucleotide = thisSeq[cursor]
        thisPair = thisSeq[cursor:cursor+2] #this is the pair we're on
    
        dimer_totals += extinction_coefficient_dictionary[thisPair]  #look up and add the dimer value
        
        if (cursor != 0 and cursor != seqLen-1): #look up and add the monomer value if we're not at the end
            monomer_totals += extinction_coefficient_dictionary[thisNucleotide]

        cursor += 1
    
    calculated_extinction_coefficient = dimer_totals - monomer_totals
    return calculated_extinction_coefficient

print "The extinction coefficient is: ",  extinctionCalc(seq_to_test, extinction_coefficient_dictionary)

#The right answer should be: 170600.0

