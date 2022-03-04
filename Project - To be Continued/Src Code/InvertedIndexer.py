# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 01:07:10 2022

@author: Lana Gharaibeh 2018902186
This code takes the frequency index we built and creates the posting lists for all documents; how ? 
- first we open all the documents in our directory(collection).
- second  we build our bag of words with all the tokens in our collection by taking the keys from the frequency
index of every document.
- thirdly we perform a loop that calls both the text processor and frequency index builder for each document .
- while the loop is running, we keep track of all tokens and in which they appear.


Project overview : we need the following for the text analysis/proccessing;
    - document processer --> In Text processor module   CHECK
    - Query processing   --> In Text processor module   CHECK
    
    - term frequency and remove reptitions --> In FrequencyIndex module CHECK
    
    - Bag of words of our whole colleection  --> In Inverted Indexer module  CHECK
    - Inverted indexer & Postings Lists      --> In Inverted Indexer module  CHECK
    
    
"""

import FrequencyIndexBuilder as fib
import TextProcessor as tpm
import os

#E:\COPIES\Desk\Autumn 2021-2022\IR Project\shakespeare
#E:\COPIES\Desk\Autumn 2021-2022\IR Project\Small Samples



def buildBagOfWords(filename,container):  #will use for boolean
    """ this function creates a long list of all the unique tokens that exist in our document collection
    """
    readyText = tpm.processText(filename)
    textFreqIndex = fib.buildFrequencyIndex(readyText)
    oneDocTokens = list(textFreqIndex.keys())
    for i in oneDocTokens:
        if i in container:
            pass
        else:
            container.append(i)
    return container 
    

def accessCollection(collectionPath):
    """ this function parses the documents in the collection from the directory
    """
    bagOfWords = []
    for filename in os.listdir(collectionPath):
        actualFilePath = os.path.join(collectionPath, filename)
        bagOfWords+= buildBagOfWords(actualFilePath, bagOfWords)
    return bagOfWords  

def buildInvertedIndex(collectionPath):
    myCollection = accessCollection(collectionPath)
    InvertedIndex = {}
    # counter = 0
    for Term in myCollection: 
        postingList = []
        for doc in os.listdir(collectionPath):
            actualFilePath = os.path.join(collectionPath, doc)
            thisDocTerms = tpm.processText(actualFilePath)
            if Term in thisDocTerms:
                postingList.append(doc)
        InvertedIndex[Term] = postingList
        # counter+=1
        # print('Iteration', counter)
    return InvertedIndex
            
def documentFrequencyPerTerm(myInvertedIndex):
    idf = {}
    for Key in myInvertedIndex:
        idf[Key] = len(myInvertedIndex[Key])
    return idf 

        
    

#Main 
# myBagOfWords = accessCollection("E:\COPIES\Desk\Autumn 2021-2022\IR Project\shakespeare")
# collectionSize = len(myBagOfWords)
# print(collectionSize) 

# IndexA = buildInvertedIndex("E:\COPIES\Desk\Autumn 2021-2022\IR Project\Small Samples")
# for Key in IndexA:
#     print(Key, "-->", IndexA[Key],"\n")


        







# class InvertedIndexEntry():
#     def __init__(self, entryValue):
#         self.entryValue = entryValue
#         self.PostingList = []
        
# class InvertedIndex(InvertedIndexEntry):
#     def buildInvertedIndex(self, indexCollectionPath):
#         collectionTokens = accessCollection(indexCollectionPath)
#         for Term in collectionTokens:
#             self.InvertedIndexEntry(Term)
#             for doc in os.listdir(indexCollectionPath):
#                 actualFilePath = os.path.join(indexCollectionPath, doc)
#                 allTermsInThisDoc = tpm.processText(actualFilePath) 
#                 if Term in allTermsInThisDoc:
#                     self.InvertedIndexEntry.PostingList.append(doc)
#             print(Term, "-->", self.InvertedIndexEntry.PostingList)
        
