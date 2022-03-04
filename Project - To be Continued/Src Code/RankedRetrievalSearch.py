# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:25:49 2022

Actual Search Engine
Ranked Retrieval 

We have : - Query                  = Query file with the query tokenized/cleaned from punct/and everything lower cased
          - Document Collection    = Inverted Index/ with postings 
          
what we have to do :
    - Calculate document frequency for each term in our collection
    - calculate term frequency per document 
    
"""

import TextProcessor as tp
import InvertedIndexer as ivd
import FrequencyIndexBuilder as fib

#E:\COPIES\Desk\Autumn 2021-2022\IR Project\shakespeare
#E:\COPIES\Desk\Autumn 2021-2022\IR Project\Small Samples


myQuery = input("Enter Your Query Here : ")

QueryFilePath = "E:\COPIES\Desk\Autumn 2021-2022\IR Project\QueryFile.txt" 
QueryFile = open(QueryFilePath, "w")
QueryFile.write(myQuery)
QueryFile.close()

myQueryCleaned = tp.processText(QueryFilePath)
print(myQueryCleaned)

testInvertedIndex = ivd.buildInvertedIndex("E:\COPIES\Desk\Autumn 2021-2022\IR Project\Small Samples")

def similarityScoring(myQueryCleaned, testInvertedIndex):
    allQueryTermScores = {}
    for qTerm in myQueryCleaned:
        tf_idf = {0} 
        if qTerm in testInvertedIndex.keys():
            term_idf_index  = ivd.documentFrequencyPerTerm(testInvertedIndex) 
            term_idf = term_idf_index[qTerm]
            matchingDocs = testInvertedIndex[qTerm] 
            for doc in matchingDocs:
                tf_index = fib.buildFrequencyIndex(doc)
                tf = tf_index[qTerm]
                doc_score = term_idf*tf
                tf_idf[doc] = doc_score 
        allQueryTermScores[qTerm] = tf_idf 
    return allQueryTermScores

print(similarityScoring(myQueryCleaned, testInvertedIndex) )


                





