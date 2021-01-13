# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:35:45 2020

@author: brayd
"""

import math

#define class similarity
class similarity:
    
    # Class instantiation
    def __init__(self, ratingP, ratingQ) :
        self.ratings1 = ratingP
        self.ratings2 = ratingQ
        
    #Minkowski Distance between two vectors
    def minkowski(self, r):
        distance = 0
        for item in self.ratings1.keys():
            if item in self.ratings2.keys():
                x = self.ratings1[item]
                y = self.ratings2[item]
                distance += pow(abs(x-y),r)
        
        return pow(distance, 1/r)
        

    # Pearson Correlation between two vectors
    def pearson(self):
        sumpq = 0
        sump = 0
        sumq = 0
        sump2 = 0
        sumq2 = 0
        n = 0
        
        for item in self.ratings1.keys():
            if item in self.ratings2.keys():
                n += 1
                p = self.ratings1[item]
                q = self.ratings2[item]
                sumpq += p * q
                sump += p
                sumq += q
                sump2 += pow(p,2)
                sumq2 += pow(q,2)
            
        nr = (sumpq - (sump*sumq) / n)
        dr = (math.sqrt(sump2 - pow(sump,2) / n) *
              math.sqrt(sumq2 - pow(sumq,2) / n))
        r = nr / dr
      
        return r
        
# User Ratings
UserPRatings = {'Motorola':8, 'LG':5, 'Sony':1, 'Apple':1, 'Samsung':5, 'Nokia':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}


Ratings = similarity(UserPRatings, UserQRatings)
manhattan = similarity.minkowski(Ratings, 1)
euclidean = similarity.minkowski(Ratings, 2)
minkowski = similarity.minkowski(Ratings, 3)
pearson = similarity.pearson(Ratings)

print(round(manhattan, 4))
print(round(euclidean, 4))
print(round(minkowski, 4))
print(round(pearson, 4))
