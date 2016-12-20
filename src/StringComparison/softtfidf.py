#!/usr/bin/env python

"""
Change Made
This module implements the soft tf-idf algorithm described in paper


This algorithm is best suited for record matching where the record is generally
smaller compared to document

Steps:
1. Compute the tf.idf score of document corpus
2. Score method return the soft tf-idf of the query against the record in the
corpus


"""

"""
Performance tips
"""

THRESHOLD = 0.9
#CORPUS = ['cat ate food','dog like food']
#CORPUS = ['apocalypse now']
import numpy as np
from  sklearn.feature_extraction.text import TfidfVectorizer
import jellyfish as jf
from collections import namedtuple

class Softtfidf():
    
    def __init__(self):
        self.tfidfvector = TfidfVectorizer(tokenizer=lambda x:x.split(" "))
   
    def buildcorpus(self,CORPUS):
        '''
        Returns sparse vector of tfidf score
        '''
        return self.tfidfvector.fit_transform(CORPUS)
        
    def builddict(self,CORPUS):
        '''
        Returns dictionary of words as key and tfidf score as value
        '''
        matrix = self.buildcorpus(CORPUS)
        vocabulary = self.tfidfvector.vocabulary_
        tfidfdict ={}
        for docId,doc in enumerate(CORPUS):
            for word in doc.split(" "):
                tfidfdict[word]=matrix[(docId,vocabulary[word])]
        return tfidfdict
    
    def score(self,s,t,CORPUS):
        '''
        Returns the similarity score
        '''
        similar = namedtuple('Similar',['r1','r2','sim'])
        similarity=[]
        tfidfdict = self.builddict(CORPUS)
        for i,ti in enumerate(s.split(" ")):
            for j,tj in enumerate(t.split(" ")):
                dist = jf.jaro_winkler(ti.decode('unicode-escape'),tj.decode('unicode-escape'))
                if dist >= THRESHOLD:
                    similarity.append(similar(i,j,
                                                 dist*tfidfdict.get(ti)* tfidfdict.get(tj)))
    
        similarity.sort(reverse=True,key=lambda x:x.sim)

        sused = np.array([False]*len(s),dtype=bool)
        tused = np.array([False]*len(t),dtype=bool)
    
    
        #check that the term are counted only once
        sim = 0.0
        for s in similarity:
            if(sused[s.r1] | tused[s.r2]):
                continue;
            sim+=s.sim
            sused[s.r1] = True
            tused[s.r2] = True
        return sim  
    
    
        


#matrix = tfidfvector.fit_transform(corpus).todense()

#tfidfvector.todense()

#features = tfidfvector.get_feature_names()

#vocabulary = tfidfvector.vocabulary_

def main():
    """ Driver program """
    #if data in kargs.keys():
    #    corpus=kargs[data]
    #getSimilarityScore('University of Moratuwa','University of Moratuwa - Faculty of Engineering')
    #for doc1,doc2 in zip(CORPUS,CORPUS):
    #    score = s.score(doc1,doc2)
    #    print(doc1,doc2,score)

def getSimilarityScore(doc1,doc2):
    CORPUS = []
    s=Softtfidf()
    CORPUS.append(doc1.lower())
    CORPUS.append(doc2.lower())
    #print(s.score(doc1.lower(),doc2.lower()))
    return s.score(doc1.lower(),doc2.lower(),CORPUS)

if __name__ == '__main__':
    main()
