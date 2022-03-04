# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:36:08 2022

@author: Lana Gharaibeh 2018902186
This code is for processing text from documents using nltk 
- it can be used for whatever search model that requires text processing, whether it is 
the boolean model or the ranked retrieval model 

Project overview : we need the following for the text analysis/proccessing;
    - document processer module--> In Text processor module   CHECK
    - Query processing module --> In Text processor module    CHECK
    
    - term frequency module and remove reptitions
    
    - Inverted indexer module 
    - 
    - document frequency module 
    
"""
# Document Processing Module 
import nltk 
from nltk import word_tokenize as wtk
import string
import re
from nltk.corpus import stopwords as stp

def readTheText(docPath): #E:\COPIES\Desk\Autumn 2021-2022\IR Project\Sample1.txt
    """ this function is for opening a text file, then saving all the text in it into a string
    variable 
    """
    myDoc = open(docPath, "r")
    stringMyDoc = myDoc.read()
    return stringMyDoc

def tokenizeTheText(myDoc):
    """ this function takes a string object and tokenizes it (from long string to a list of tokens)
    """
    return wtk(myDoc)
    
def removePunct(myDoc): 
    """ this function removes the punctuation from the text string(needs to be already tokenized)
    """
    myDocNoPunct = [ x for x in myDoc if not re.fullmatch("[" + string.punctuation + "]", x)]
    return myDocNoPunct

def lowerText(myDoc):
    """ this function is for making all the text letters lowered for unification of words
    """
    myDocLowered = [ token.lower() for token in myDoc]
    return myDocLowered
    
def removeStopwords(myDoc):
    """ this function is for removing stopwords from the tlist of tokenized, cleaned and lowered text
    """
    Stop_words = stp.words("english")
    filteredText = []
    for i in myDoc :
        if i not in Stop_words :
            filteredText.append(i)
    return filteredText
    
def processText(myDocPath):
    sampleText = readTheText(myDocPath)                         #read text and store it in var
    sampleTextTokenized = tokenizeTheText(sampleText)           #tokenize text
    tokenizedTextCleaned = removePunct(sampleTextTokenized)     #remove all punctuations
    cleanTokenizedLowered = lowerText(tokenizedTextCleaned)     #lowercase all tokens
    readyText = removeStopwords(cleanTokenizedLowered)          #remove all stopwords
    return readyText

#Main
sampleText = readTheText("E:\COPIES\Desk\Autumn 2021-2022\IR Project\Small Samples\Sample1.txt")
print(sampleText)
print("---------------------------")

sampleTextTokenized = tokenizeTheText(sampleText)
print(sampleTextTokenized)
print("---------------------------") 

tokenizedTextCleaned = removePunct(sampleTextTokenized)
print(tokenizedTextCleaned)
print("---------------------------")

cleanTokenizedLowered = lowerText(tokenizedTextCleaned)
print(cleanTokenizedLowered)

print("---------------------------")
readyText = removeStopwords(cleanTokenizedLowered)
print(readyText)
myText = processText("E:\COPIES\Desk\Autumn 2021-2022\IR Project\Sample1.txt")
print(myText)



























