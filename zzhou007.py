﻿#-------------------------------------------------------------------------------
# Author:      amir
# Created:     10/25/2015
#
# Instructions:
#
# 1) Make sure to rename the file (studentNetId.py) to your netId. (Do not include your first name, last name ... or any extra character)
# 2) To run the program type the following statement in the command line:  
#       -) python studentNetId.py DNASeq1FilePath DNASeq2FilePath OutputFilePath                                                                   
#    where  DNASeq1FilePath is the path to the file that contains First DNA sequence (e.g. DNASeq1.txt)
#           DNASeq2FilePath is the path to the file that contains Second DNA sequence (e.g. DNASeq2.txt)
#           OutputFilePath is the path that the output is goint to be saved (e.g. out.txt)
# 3) Make sure to replace FirstName, LastName, SectionNumber, NetId in studentInfo with your information
# 4) You may add as many functions as you want to this program
# 5) The core function in your program is DNASeqAlignment function, where it takes three arguments (DNASeq1,DNASeq2,outputPath) and 
#    computes the similarityScore, sequenceAlignment1 and sequenceAlignment2. At the end, the function writes the result to the output file (Do not make any changes to the output section).
# 6) sequenceAlignment1 and sequenceAlignment2 are strings and they are composed of following characters: 'A', 'T', 'G', 'C' and '-', Do not include extra space or any other character in the strings.
# 7) Make sure your program works with at least one of the following python versions: (2.7.9, 2.7.8, 2.6.6)
# 8) Once you have tested your program with one of the versions listed above, assign that version number to pythonVersion in studentInfo function
# 9) Make sure to write enough comments in order to make your code easy to understand. 
# 10) Describe your algorithm in ALGORITHM section below (you may add as many lines as you want).
# 11) To understand the flow of the program consider the following example:
#      0) Let say we have DNASeq1.txt file which contains AACCTGACATCTT and DNASeq2.txt file contains CCAGCGTCAACTT
#      1) If we execute the following command in the command line: -) python studentNetId.py DNASeq1.txt DNASeq2.txt out.txt
#      2) input arguments are parsed       
#      3) studentInfo() function will be executed and the output will be saved in out.txt file
#      4) DNASeqAlignment() function will be called
#      5) At the entry of the DNASeqAlignment function, DNASeq1='AACCTGACATCTT' and DNASeq2='CCAGCGTCAACTT'
#      6) You should compute the sequence alignment of DNASeq1 and DNASeq2. Let say the result is as follows:
#       A A C C T G A C - - - - A T C T T
#       | | | | | | | | | | | | | | | | |
#       - - C C A G - C G T C A A - C T T      
#      7) At the end of the DNASeqAlignment function sequenceAlignment1='AACCTGAC----ATCTT', sequenceAlignment2='--CCAG-CGTCAA-CTT', similarityScore=6.25
#      8) In the output section the result is going to be saved in out.txt file
#-------------------------------------------------------------------------------

# ALGORITHM: 
#
#
#
#
#


import os
import sys
import argparse

def studentInfo():
    pythonVersion = '2.7.9'
    studentFirstName = "Zihang"
    studentLastName = "Zhou"
    studentSectionNumber = "2"
    studentNetId = "zzhou007"
    info = 'FirstName: ' + studentFirstName + '\n'
    info = info + 'LastName: ' + studentLastName + '\n'
    info = info + 'Section: ' + studentSectionNumber + '\n'
    info = info + 'NetId: ' + studentNetId + '\n'
    info = info + 'Python version: ' + pythonVersion + '\n'
    return info
def calc(i, j, DNA1, DNA2):
    if (DNA1[i] == DNA2[j]):
	    return 1
    elif (DNA1[i] == "A" and DNA2[j] == "T"):
    	    return -0.15
    elif (DNA1[i] == "T" and DNA2[j] == "A"):
    	    return -0.15
    elif (DNA1[i] == "G" and DNA2[j] == "C"):
    	    return -0.15
    elif (DNA1[i] == "C" and DNA2[j] == "G"):
    	    return -0.15
    else:
	    return -0.1
    
	

def DNASeqAlignment(DNASeq1,DNASeq2,outputPath):
    similarityScore = -1
    sequenceAlignment1 = ''
    sequenceAlignment2 = ''
    #########################################################################################
    # Compute new values for similarityScore and sequenceAlignment1 and sequenceAlignment2  #                                                                  #
    #########################################################################################
#x and y coord for table
    x = len(DNASeq1) + 1 
    y = len(DNASeq2) + 1
#populate list l
    l = [[0 for i in range(x)] for j in range(y)]
#print sides     
    for i in range(x):
	    l[i][0] = 0 - 0.2*i
    for i in range(y):
	    l[0][i] = 0 - 0.2*i
#fill list get max of 3 items 
    for i in range(1, x):
	    for j in range(1, y):
		    remove = l[i - 1][j] - 0.2
		    insert = l[i][j - 1] - 0.2
		    sub = calc(i - 1, j - 1, DNASeq1, DNASeq2) + l[i - 1][j - 1]
		    if remove > insert and remove > sub:
		    	l[i][j] = remove
		    elif insert > remove and insert > sub:
		    	l[i][j] = insert
		    else:
			l[i][j] = sub
		    if l[i][j] < .00000000001 and l[i][j] > -.0000001:
			l[i][j] = 0
    similarityScore = l[x - 1][y - 1]

    #################################  Output Section  ######################################
    result = "Similarity score: " + str(similarityScore) + '\n'
    result = result + "Sequence alignment1: " + sequenceAlignment1 + '\n'
    result = result + "Sequence alignment2: " + sequenceAlignment2 + '\n'
    writeToFile(outputPath,result)
    
def writeToFile(filePath, content):
    with open(filePath,'a') as file:
        file.writelines(content)

def readFile(filePath):
    logLines = ''
    with open(filePath,'r') as file:
        for logText in file:
            logLines = logLines + logText

    uniqueChars = ''.join(set(logLines))
    for ch in uniqueChars:
        if ch not in ('A','a','C','c','G','g','T','t'):
            logLines = logLines.replace(ch,'')
    logLines = logLines.upper()
    return logLines

def removeFile(filePath):
    if os.path.isfile(filePath):
        os.remove(filePath)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DNA sequence alignment')
    parser.add_argument('DNASeq1FilePath', type=str, help='Path to the file that contains First DNA sequence')
    parser.add_argument('DNASeq2FilePath', type=str, help='Path to the file that contains Second DNA sequence')
    parser.add_argument('OutputFilePath', type=str, help='Path to the output file')
    args = parser.parse_args()
    DNASeq1 = readFile(args.DNASeq1FilePath)
    DNASeq2 = readFile(args.DNASeq2FilePath)
    outputPath = args.OutputFilePath
    removeFile(outputPath)
    writeToFile(outputPath,studentInfo())
    DNASeqAlignment(DNASeq1,DNASeq2,outputPath)
