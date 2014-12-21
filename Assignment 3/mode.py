# -*- coding: utf-8 -*-
# Python Problem 3
#mode.py
#Introduction to Bioinformatics Assignment 2
#Purpose: Find the mode
#Your Name: Diane Kaplan
#Date: October 4, 2014

#will contain all the data of a list including some unwanted carriage return symbols
tempList = []
#will contain the data after it is stripped and the header is removed
myData = []
#will store the header
header = ""
#this will store the value of the mode
mode = 0

#TASK1
#We have the file data.txt read all the values of this file in the list tempList
fileName = "data.txt"
tempList = []
text_file = open(fileName, 'r') #r means open it for reading, w is for writing
#or could have just done this:  text_file = open("mycExpres.txt", 'r')
tempList = text_file.readlines()
text_file.close()

#We don't want the header to be in the list Pop it and save it into the header variable
header = tempList.pop(0).strip()

#for every member of tempList, clean it up from carriage return, convert it into a float and add it to the list myData
myData = [float(value.strip()) for value in tempList]

#Sort the list
myData.sort()

#The mode of a dataset is the number that occurs most frequently.

#current value we're counting (initialized to 0.0)
lastValue = 0.0

#counter for that current value (initialized to 0)
numCounter = 0

#placeholder for the winning value (initialized to 0)
mode = 0

#placeholder for the winning count (initialized to 0)
bestCounter = 0
 
 #Count the frequency for each value in the list.  Because the list is sorted, count fresh when the value changes from the last one.   
for element in myData:
    if element != lastValue: #this is a new value, let's count it
        lastValue = element
        numCounter = myData.count(element)     
        if numCounter > bestCounter:  #if the count is higher than previous best, that value and count replace the previous bests
            bestCounter = numCounter
            mode = element

print "The mode of the:", header, "dataset is:", mode     

