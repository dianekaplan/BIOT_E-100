# -*- coding: utf-8 -*-
#align.py
#Introduction to Bioinformatics
#Python Assignment 5, Problem 2
#Purpose: Compare a sequence to mouse mRNA: get 20mers and identify the one with the best score
#Your Name: Diane Kaplan
#Date: December 5, 2014

import Bio
from Bio import Entrez
from Bio import SeqIO
from Bio import pairwise2  #tried this for scoring below, but my laptop wasn't having it
import pickle
from assignment5_shared_functions import reverseComplement
from assignment5_shared_functions import make_Nmers_list

#FIRST DEFINE OUR FUNCTIONS

#Function takes a list of Nmers, scores them (by calling get_score function), and pickles results for reference/troubleshooting
def score_and_save_Nmers(Nmer_list, comparison_seq):  #calls get_score function
    Nmer_score_dictionary = {}
      
    for Nmer in Nmer_list:
            Nmer_score_dictionary [Nmer] = get_score(Nmer,comparison_seq)
            
    pickle.dump(Nmer_score_dictionary, open( "Nmer_scores.dict", "wb" ) )
    return Nmer_score_dictionary    
    

#Function scores two sequences, using scheme of: +1 for a match and -1 for a mismatch
def get_score(comparison_oligo, mRNA_seq):
    
    seq1 = comparison_oligo
    seq2 = mRNA_seq
    score = 0    
    #match=1
    #mismatch=-1
    
    for a, b in zip(seq1,seq2): 
    	if a==b:
	   score +=1
	else: 
	    score -=1 
	    
	#I ALSO TRIED USING THIS, BUT IT HUNG/CRASHED CANOPY
        #aln = pairwise2.align.localmx(seq1, seq2, match, mismatch)
        #top_aln = aln[0]
        #score = top_aln[2]

    return score


#NOW LET'S DO STUFF
    
#Using Biopython, get the mRNA sequence of mouse Apolipoprotein B : NM_009693.2  GI: 161702987 
Entrez.email = "A.N.Other@example.com"
handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="161702987") 
seq_record = SeqIO.read(handle, "fasta")
handle.close()

#Save the sequence record locally as a string
mouse_Apolipoprotein_B_mRNA = seq_record.seq
mouse_Apolipoprotein_B_mRNA = str(mouse_Apolipoprotein_B_mRNA)

#The drug we're comparing with, reversed to the 3' to 5' strand
comparison_seq= 'GCCTCAGTCTGCTTCGCACC'
comparison_seq= reverseComplement(comparison_seq)

nmers_list = make_Nmers_list(mouse_Apolipoprotein_B_mRNA, 20)
score_and_save_Nmers(nmers_list, comparison_seq)

saved_dictionary = pickle.load( open( "20mer_scores.dict", "rb" ) )

#Found this hint on stackoverflow to get the highest score and Nmers that have it (in case of a tie)
winning_score = max(saved_dictionary.values())            
keys = [x for x,y in saved_dictionary.items() if y ==winning_score] 

print "The best score is: " , winning_score
print "The 20mer(s) with that score: " , keys 
