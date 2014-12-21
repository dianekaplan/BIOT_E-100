# -*- coding: utf-8 -*-
#refSeqmRNA.py
#Introduction to Bioinformatics Assignment 4
# Python Problem 1
#Purpose: 
#Your Name: Diane Kaplan
#Date: October 17, 2014
#Citations: 
#used section notes for parsing Fasta file
#http://pymotw.com/2/pickle/

import string #have this for the rstrip stuff below that I haven't used yet- remove this if we don't use it later
import pickle

#TASK 1
#Read values from human.rna.fna into the list tempList
fileName = "human.rna.fna"
tempList = []
text_file = open(fileName, 'r') #r means open it for reading, w is for writing
#or could have just done this:  text_file = open("mycExpres.txt", 'r')
tempList = text_file.readlines()
text_file.close()

#Make a string out of these lines
big_string_of_data = "".join(line.strip() for line in tempList)

#split it into a list of strings, one for each sequence
list_of_fasta_strings = big_string_of_data.split(">")
#note, the first index has nothing in it

##Loop through and process each sequence

#create the dictionaries I'll be adding into
#Note all keys and values should be strings

giToRefSeq = {} #given the gi number as a string returns the RefSeqID
refSeqToGi = {} #given the refSeqID without version returns the gi number
giToName = {} #given the gi number returns the name of the gene
refSeqToName = {} #given the RefSeqID without version returns the name of the gene
giToSeq = {} #given the gi number returns the sequence
refSeqToSeq = {} #given the refSeqID without version returns the sequence of the gene

#take each string and break out the parts
for fasta_string in list_of_fasta_strings:
    parts = fasta_string.split("|")
    #print parts[0], parts[-1] 
    #I should be able to grab pieces by index and save, but IndexError (list index out of range) for parts[1], etc
        #this_GI = parts[1]
        #this_RefSeqID = parts[3]
        #print len(parts)
        #this_gene = parts[4]
        #this_sequence = parts[5] 
    thiscursor = 0
    this_GI = ''
    this_RefSeqID = ''
    this_gene_and_seq = ''
    for part in parts:  #THIS WAY DOES SHOW ME ALL THE PARTS- so why does accessing the indexes only work for the first?
        if thiscursor == 1:
            this_GI = part
        if thiscursor ==3:
            this_RefSeqID = part
        if thiscursor == 4: 
            this_gene_and_seq = part
        thiscursor +=1
     
    #remove the version number from RefSeqID- I couldn't get it to strip or rstrip stuff after the ., so I split :\   
    #this_RefSeqID = string.replace (this_RefSeqID, '.*', '')
    #this_RefSeqID = this_RefSeqID.rstrip('/.*/')
    temp = this_RefSeqID.split('.')
    this_RefSeqID = temp[0]
    print this_RefSeqID
    
    ###split the gene & sequence  
    this_gene = ''
    this_seq = ''
    #this_gene_and_seq = this_RefSeqID.split('.')
    #this_RefSeqID = temp[0]
    #print this_RefSeqID  
                  
    #print "this GI: " , this_GI
    #print "this RefSeqID: " , this_RefSeqID
    #print "this gene: " , this_gene_and_seq
    giToRefSeq[this_GI] = this_RefSeqID
    refSeqToGi[this_RefSeqID] = this_GI
    giToName[this_GI] = this_GI
    

