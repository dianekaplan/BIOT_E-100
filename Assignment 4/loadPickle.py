# -*- coding: utf-8 -*-
#loadPickle.py
#Introduction to Bioinformatics Assignment 4
# Python Problem 12
#Purpose: 
#Your Name: Diane Kaplan
#Date: October 17, 2014
#Citations: wiki.python.org for pickle example

import pickle

#Load each of the dictionaries we made
giToRefSeq = pickle.load( open( "giToRefSeq.dict", "rb" ) )
refSeqToGi = pickle.load( open( "refSeqToGi.dict", "rb" ) )
giToName = pickle.load( open( "giToName.dict", "rb" ) )
refSeqToName = pickle.load( open( "refSeqToName.dict", "rb" ) )
refSeqToSeq = pickle.load( open( "refSeqToSeq.dict", "rb" ) )

#Output example entries so we know we have it
print giToRefSeq["324073531"] 
print refSeqToGi["NM_177422"]
print giToName["324073531"] 
print refSeqToName["NM_177422"]
print refSeqToSeq["NM_177422"]