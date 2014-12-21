# -*- coding: utf-8 -*-
#translate.py
#Introduction to Bioinformatics Assignment 4
# Python Problem 1
#Purpose: get a sequence from the net using Biopython
#Your Name: Diane Kaplan
#Date: October 18, 2014
#citations: none

import Bio
from Bio import Entrez
from Bio import SeqIO

#Use the GI number of the human FOXP2 gene to get the FOXP2 sequence
Entrez.email = "A.N.Other@example.com"
handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="298566293") 
seq_record = SeqIO.read(handle, "fasta")
handle.close()

#Save the sequence record locally
seqFOXP2 = seq_record.seq

#Use the CDS coordinatates (375..2519) from here: http://www.ncbi.nlm.nih.gov/nuccore/NM_001172766
#Make 3 subsequence Objects from the seqFOXP2 mrna sequence
seqFOXP2_5UTR = seqFOXP2[0:374]
seqFOXP2_3UTR = seqFOXP2[2519:]
seqFOXP2_Coding = seqFOXP2[374:2519] #Subtract 1 since we start at 0 (and still use 2519 for the end because slice is UP TO that point)

print "The length of the coding part (seqFOXP2_Coding) is:" , len(seqFOXP2_Coding)
print "The sum of the lengths of seqFOXP2_5UTR, seqFOXP2_3UTR and seqFOXP2_Coding is: " , (len(seqFOXP2_5UTR) + len(seqFOXP2_3UTR) + len(seqFOXP2_Coding))

#Run the translate() function on the seqFOXP2_Coding object.
translated_FOXP2 = seqFOXP2_Coding.translate()
print "The translated protein sequence is: ", translated_FOXP2

print "Note: I can remove that trailing asterisk when I include one less character in seqFOXP2, but it's then no longer a multiple of 3"