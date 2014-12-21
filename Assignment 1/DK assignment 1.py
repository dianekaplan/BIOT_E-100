#Diane Kaplan
#BIOT E-100 
#Assignment 1, Python questions
#citations: I checked syntax in class notes and lessons on codeacademy.com, practical computing book reminded me of whitespace and .2f, 
#and got the syntax for returning the 3 stop counters together on stackoverflow
   
#Program 1
#
#The amount of "GC content" is one of the signals that there is a gene present. http://en.wikipedia.org/wiki/GC-content#GC_ratio_of_genomes
#Write a small program called GCcontent.py to calculate the combined percentage of "C"s and "G"s in a sequence. Your calculation should be:
#percent GC content = 100 * (number of "C"s + number of "G"s) / (length of sequence)

def GCcontent (seq):   #function takes a sequence and returns the %age of characters that are C's and G's
    DesiredBases=["C","G"]
    Length= len(seq)
    GCcounter = 0
    GCresult = 0
    for char in seq:  #loop through the string and tally the C's & G's
        if char in DesiredBases:
            GCcounter += 1  
    GCresult = "%.2f" % (100 * GCcounter/float(Length)) #cast the length as a float to preserve decimal, then use .2f to keep it to 2 places
    return GCresult

#Program 2
#
#Another signal of a gene is called "CpG islands". The "p" refers to the phosphodiester bond connecting the cytosine to the guanine nucleotide, reading in the normal 5' to 3' direction. http://en.wikipedia.org/wiki/CpG_site#CpG_islands
#So you want to count "CG" dimers in a sequence. Write a small program called CpGcount.py to do that.

def CpGcount (seq):       #function takes a sequence and returns the number of "CG" instances found in it
	Length = len(seq)
	DesiredSubstring="CG"
	CpGcounter = 0
	CpGresult = 0
	cursor = 0
	
	while cursor < (Length-1):
	       tempstring = seq[cursor:(cursor+2)]
               if tempstring == "CG":	#check our current pair for a match, and move along
	           CpGcounter += 1  
	       cursor += 1
	CpGresult = CpGcounter 
	return CpGresult 

#Program 3
#
#Count the number of STOP codons is a given sequence. Consider all three possible STOP codons, but just scan reading frame 1 for them. Write a small program called CountSTOPs.py to do that.

def CountSTOPs (seq):     #function takes a sequence and returns the number STOP codons, with breakdown of which ones
	Length = len(seq)
	StopCodons=["TAG", "TAA", "TGA"] 
	stopcounter = 0  #total number of stop codons
	TAGcounter=0
	TAAcounter=0
	TGAcounter=0

	cursor = 0
	iterations=0
	loopCount = (Length/3) #Loop through as many times there are triplets. (Alternative would be: loop while the cursor is >=3 from the end)
	
	while iterations < loopCount:  
	       tempstring = seq[cursor:(cursor+3)]
               if tempstring in StopCodons:
                    stopcounter += 1  
                    if tempstring=="TAG":
                      TAGcounter +=1 
                    elif tempstring=="TAA":
                       TAAcounter+=1 
                    elif tempstring=="TGA":  #if we're here it should only be TGA, but overkill for readability later
                       TGAcounter+=1 
	       iterations +=1
	       cursor += 3     #we're only reading frame 1, so we'll advance 3 at a time

	return {'Total stop codons:':stopcounter,'TAG:':TAGcounter, 'TAA:':TAAcounter, 'TGA:':TGAcounter}  

	
seq = raw_input("Let's measure GC content, CG dimers, and codon stops.  Please type a short sequence and hit return: ")  
seq = seq.upper()  #capitalize string for comparison
seq = seq.replace(" ","") #remove whitespace if there is any
ThisGCresult = GCcontent(seq)
ThisCpGresult = CpGcount(seq)
TheseSTOPcodons = CountSTOPs(seq)

print "For this sequence, the GC ratio is:", ThisGCresult, "%"
print "The CpGcount (number of 'CG' dimers) is:", ThisCpGresult
print "The total number of stop codons is:", TheseSTOPcodons

