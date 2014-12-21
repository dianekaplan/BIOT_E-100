# -*- coding: utf-8 -*-
#filters.py
#Introduction to Bioinformatics
#Python Assignment 5, Problem 3
#Purpose: Generate candidate Nmers, filter out the lower quality ones, and find those cross-reactive between human & mouse
#Your Name: Diane Kaplan
#Date: December 5, 2014

import Bio
from Bio import Entrez
from Bio import SeqIO
from assignment5_shared_functions import reverseComplement
from assignment5_shared_functions import make_Nmers_list

#FIRST DEFINE OUR FUNCTIONS

# getAllNMers takes as an argument a sequence string and a number n that represents the length of the antisense oligonucleotides 
#to design and returns a list of the reverse complements of every possible n-mer made from the provided sequence. 
def getAllNMers(sequence,n): #calls make_Nmers_list and reverseComplement functions
    
    plain_Nmer_list = make_Nmers_list (sequence, n)
    reversed_Nmer_list = [reverseComplement(nmer) for nmer in plain_Nmer_list]

    return reversed_Nmer_list
    
#Function takes a list of sequences and removes any with 4+ contiguous G's. Return cleaned list.
#Citation: docs.python.org told me about find (returns the index where the substring is, -1 if not there, so only keep if answer < 0)
def filter4G(mylist): 
    cleaned_list = []  #here's where we'll store the good ones

    for each in mylist:
        cleaned_list = [each for each in mylist if each.find('GGGG') < 0]
    return cleaned_list
    
#Tried putting it in shared functions file, but kept getting error when adding up top "ImportError: cannot import name gc_content "
def gc_content (seq):   #function takes a sequence and returns the %age of characters that are C's and G's
    DesiredBases=["C","G"]
    Length= len(seq)
    GCcounter = 0
    GCresult = 0
    for char in seq:  #loop through the string and tally the C's & G's
        if char in DesiredBases:
            GCcounter += 1  
    GCresult = 100 * GCcounter/float(Length) #cast as float to preserve decimal
    return GCresult
    
#Function takes a list and n, a float that specifies the lower cutoff limit for GC content. Only keep those with N or better. 
def filterGC(mylist, n): 
    cleaned_list = []  #list to store the sequences above threshold gc content

    for seq in mylist:
        cleaned_list = [seq for seq in mylist if gc_content(seq) > n]
    return cleaned_list

    
#NOW LET'S DO STUFF
#Using Biopython, get the human Apolipoprotein B human mRNA sequence:
Entrez.email = "A.N.Other@example.com"
handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="105990531") 
seq_record = SeqIO.read(handle, "fasta")
handle.close()

#Save the sequence record locally as a string
human_Apolipoprotein_B_mRNA = seq_record.seq
human_Apolipoprotein_B_mRNA = str(human_Apolipoprotein_B_mRNA)

#JUST FOR TESTING, TAKE OUT LATER**************************
#human_Apolipoprotein_B_mRNA = human_Apolipoprotein_B_mRNA[0:1500]

#Use the human Apo B mRNA sequence  and n=20. Run your function and Save the output in a list called allNmers.
allNmers = getAllNMers(human_Apolipoprotein_B_mRNA, 20)

#REPORT: Length of allNmers and print allNmers   (2 points)
print "REPORT: Length of allNmers and print allNmers"
print len(allNmers) , allNmers

#Run your function using allNmers as input and Save the output of this result in a list called noGGGG.
noGGGG = filter4G(allNmers)

#REPORT: Length of noGGGG and print noGGGG (2 points)
print "REPORT: Length of noGGGG:"
print len(noGGGG) #, noGGGG

#Run your function using noGGGG as input and a 50.0 lower GC content cutoff.  Save the output of this result in a list called gc50.
gc50 = filterGC(noGGGG, 50.0)

#REPORT: Length of gc50 (2 points)
print "REPORT: Length of gc50:"
print len(gc50) #, gc50

gc50 = set(gc50)
#print 'Minus the dupes, people have:', len(gc50) #, gc50

#Find the molecules from gc50 that are completely cross-reactive (identical) to the mouse Apolipoprotein B mRNA sequence
    
#Using Biopython, get the mRNA sequence of mouse Apolipoprotein B : NM_009693.2  GI: 161702987 
Entrez.email = "A.N.Other@example.com"
handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="161702987") 
seq_record = SeqIO.read(handle, "fasta")
handle.close()

#Save the sequence record locally as a string
mouse_Apolipoprotein_B_mRNA = seq_record.seq
mouse_Apolipoprotein_B_mRNA = str(mouse_Apolipoprotein_B_mRNA)

#JUST FOR TESTING, TAKE OUT LATER*****************************************
#mouse_Apolipoprotein_B_mRNA = mouse_Apolipoprotein_B_mRNA[0:1500]

#Get the list of Nmers for the mouse mRNA
allNmers_mouse = getAllNMers(mouse_Apolipoprotein_B_mRNA, 20)

#REPORT: Length of allNmers and print allNmers   (2 points)
print "REPORT: Length of allNmers_mouse:"
print len(allNmers_mouse) # , allNmers_mouse

#As before, filter out the ones with 4+ G's
noGGGG_mouse = filter4G(allNmers_mouse)

#REPORT: Length of noGGGG and print noGGGG (2 points)
print "REPORT: Length of noGGGG_mouse:"
print len(noGGGG_mouse) #, noGGGG_mouse

#As before, filter out the ones below 50% GC content
gc50_mouse = filterGC(noGGGG_mouse, 50.0)

#REPORT: Length of gc50 (2 points)
print "REPORT: Length of gc50_mouse"
print len(gc50_mouse) #, gc50_mouse

gc50_mouse = set(gc50_mouse)
#print 'Minus the dupes, mice have:' , len(gc50_mouse) #, gc50_mouse

#make a set of all these 
gc50_human_mouse_intersection = gc50.intersection(gc50_mouse)

print 'In common, there are this many identical:' 
print len(gc50_human_mouse_intersection) , gc50_human_mouse_intersection