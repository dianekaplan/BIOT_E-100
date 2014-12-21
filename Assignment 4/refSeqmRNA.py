# -*- coding: utf-8 -*-
#refSeqmRNA.py
#Introduction to Bioinformatics Assignment 4
# Python Problem 1
#Purpose: 
#Your Name: Diane Kaplan
#Date: October 17, 2014
#Citations: section notes for parsing Fasta file, biopython docs for usage, converting seq to string, 
#http://pymotw.com/2/pickle/ and wiki.python.org for pickle example

import Bio
from Bio import SeqIO
import pickle

#Read values from human.rna.fna into the list tempList
fileName = "human.rna.fna"
text_file = open(fileName, 'r') #r means open it for reading, w is for writing
tempList = text_file.readlines()
text_file.close()

#Create the dictionaries I'll be adding into
giToRefSeq = {} #given the gi number as a string returns the RefSeqID
refSeqToGi = {} #given the refSeqID without version returns the gi number
giToName = {} #given the gi number returns the name of the gene
refSeqToName = {} #given the RefSeqID without version returns the name of the gene
giToSeq = {} #given the gi number returns the sequence
refSeqToSeq = {} #given the refSeqID without version returns the sequence of the gene

#We have a string for each fasta record.  Loop through each, 
#grab the relevant parts, and create dictionary entries we'll need
for seq_record in SeqIO.parse("human.rna.fna", "fasta"):
    this_combined_info = seq_record.description
    temp = this_combined_info.split('|')
    
    #Split out relevant pieces of data from the description, and save the sequence as a string
    this_GI = temp[1]
    this_ReqSeqIDwithVersion = temp[3]
    this_gene = temp[4]
    this_seq_as_object = seq_record.seq
    this_seq_as_string = str(this_seq_as_object)
    
    #Split to remove version (couldn't figure out a way using rstrip)
    RefSeqtemp = this_ReqSeqIDwithVersion.split('.')
    this_RefSeqID = RefSeqtemp[0]
    
    giToRefSeq[this_GI] = this_RefSeqID
    refSeqToGi[this_RefSeqID] = this_GI
    giToName[this_GI] = this_gene
    refSeqToName[this_RefSeqID] = this_gene
    giToSeq[this_GI] = this_seq_as_string
    refSeqToSeq[this_RefSeqID] = this_seq_as_string    

#Now that we have all the dictionary entries, pickle dump to use later
pickle.dump(giToRefSeq, open( "giToRefSeq.dict", "wb" ) )
pickle.dump(refSeqToGi, open( "refSeqToGi.dict", "wb" ) )
pickle.dump(giToName, open( "giToName.dict", "wb" ) )
pickle.dump(refSeqToName, open( "refSeqToName.dict", "wb" ) )
pickle.dump(giToSeq, open( "giToSeq.dict", "wb" ) )
pickle.dump(refSeqToSeq, open( "refSeqToSeq.dict", "wb" ) )

#Output example entries so we know we have it
print giToRefSeq["324073531"] 
print refSeqToGi["NM_177422"]
print giToName["324073531"] 
print refSeqToName["NM_177422"]
print refSeqToSeq["NM_177422"]