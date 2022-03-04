# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 00:03:54 2022

@author: Lana Gharaibeh 2018902186
This code takes a pre-processed document text and removes the repititions of words after counting how many times
they appeared in the text.

Project overview : we need the following for the text analysis/proccessing;
    - document processer --> In Text processor module   CHECK
    - Query processing   --> In Text processor module   CHECK
    
    - term frequency and remove reptitions --> In FrequencyIndex module CHECK
    
    - Inverted indexer & Postings Lists --> 
    - document frequency module 

"""
import TextProcessor as tpm

def buildFrequencyIndex(myDoc):
    """ this function takes a list of tokens produced by the text processor module and parses all the tokens, 
    counting the instances of each token in the list to calculate the term frequency in the document and uses a 
    python dictionary to organize each token(key) with its term frequency in the document (value)
    """
    termFrequencyGrouped = {}
    for i in myDoc:
        if i in termFrequencyGrouped:
            pass
        else:
            tf = myDoc.count(i)
            termFrequencyGrouped[i] = tf
    return termFrequencyGrouped   


#Main
# sampleText = tpm.processText("E:\COPIES\Desk\Autumn 2021-2022\IR Project\Sample1.txt") 
# FrequencyIndex = buildFrequencyIndexOneDoc(sampleText)
# print(FrequencyIndex)



    

