# -*- coding: utf-8 -*-
#Python Problem 1
#reverseComplement.py
#Introduction to Bioinformatics Assignment 2
#Purpose: A simple exercise for using a for loop and if statements
#Your Name: Diane Kaplan
#Date: October 4, 2014

#s1 is the string you should use to generate a reverse complement sequence
#s1Backward is the string for storing the same bases in reverse order
#basePartners is a little dictionary for complementary bases
#s1converted is the string to store our converted complementary sequence
s1 = "AAAAACCCCCTCGGCTAATCGACTACTACTACTACTACTTCATCATCATCAGGGGGGGGCTCTCTCTAAAAACCCCTTTTGGGGG"
s1_backward = s1[::-1] 
base_partners = {"A":"T", "C":"G", "G":"C", "T":"A"} 
s1_converted = ""  

#Loop through and look up the complement to create the new sequence
for char in s1_backward:
    s1_converted += base_partners[char]

print "Starting with this sequence:", s1
print "Its reverse complement is: ", s1_converted
