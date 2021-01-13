# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:14:06 2020

@author: brayd
"""

print ()
import math 
from operator import itemgetter
# define class similarity
class similarity:   
    
    # Class instantiation    
    def __init__ (self, ratingP, ratingQ):       
        self.ratings1 = ratingP       
        self.ratings2 = ratingQ    
        
    # Minkowski Distance between two vectors  
    def minkowksi(self, r):       
        # calculate minkowski distance  
        distance = 0            
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            p = self.ratings1[k]          
            q = self.ratings2[k]        
            distance += pow(abs(p - q), r)   
            # return value of minkowski distance 
        return pow(distance,1/r)  
        
    # Pearson Correlation between two vectors  
    def pearson(self):       
        sumpq = 0       
        sump = 0       
        sumq = 0      
        sump2 = 0     
        sumq2 = 0     
        n = 0       
    # calculate pearson correlation using the computationally efficient form    
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):       
            n += 1       
            p = self.ratings1[k]    
            q = self.ratings2[k]     
            sumpq += p * q         
            sump += p          
            sumq += q           
            sump2 += pow(p, 2)   
            sumq2 += pow(q, 2)    
    # error check for n==0 condition  
        if n == 0:           
            print (">>> pearson debug: n=0; returning -2 correlation!")      
            return -2    
                    
                    
    # calculate nr and dr for pearson correlation   
        nr = (sumpq - (sump * sumq) / n)       
        dr = (math.sqrt(sump2 - pow(sump, 2) / n) *
                         math.sqrt(sumq2 - pow(sumq, 2) / n))  
        # error check for dr==0 condition 
        if dr == 0:          
            print (">>> pearson debug: denominator=0; returning -2 correlation!") 
            return -2       
        # return value of pearson correlation coefficient     
        return nr / dr
# user ratings
songData3 = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},   
             "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},  
             "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0}, 
             "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},  
             "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0}, 
             "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
             "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},  
             "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}        
             }
# for whom are we making recommendations?
userX = "Hailey"
userXRatings = songData3[userX]

# find the euclidean distance between userX's ratings, and each of the other user's ratings.
# use a for loop to get at the other users and their ratings - DO NOT hard code.
# use the similarity class to caclulate the euclidean distance between user ratings.
# assign list of (user, distance) tuples to variable userDistances.
# Example: [('Jordyn', 4.39), ('Chan', 3.16), ('Veronica', 1.41), ('Bill', 3.64)]

# Code Chunk 1
userDistances = []
for userY, userYRatings in songData3.items(): 
    if (userX != userY):
        Ratings = similarity(songData3[userY], songData3[userX])
        euclidean = round(similarity.minkowksi(Ratings, r = 2),2)
      
        userDistances.append((userY, euclidean))
        
        
print(userDistances)




# sort list of tuples by lowest distance to highest distance.
# assign sorted list to variable userSortedDistances.
# Example: [('Veronica', 1.41), ('Sam', 2.45), ('Angelica', 2.74)]

# Code Chunk 2
userSortedDistances = []
userSortedDistances.append(sorted(userDistances, key=itemgetter(1), reverse=False))
print()
print(userSortedDistances)


# userX's NN is the user at the 0th position of the sorted list.
# assign NN to userXNN.
# Example: 'Veronica'

# Code Chunk 3
userXNN = ""
userXNN = userSortedDistances[0][0][0]
print()
print(userXNN)

# recos for userX will include albums rated by userXNN, not already rated by userX.
# assign list of (album, rating) tuples to variable userXRecos.
# Example: [('Slightly Stoopid', 2.5), ('Blues Traveler', 3.0), ('Phoenix', 4.0)]

# Code Chunk 4
userXRecos = []

for album, rating in songData3[userXNN].items():
    if album not in songData3[userX].keys():        
        userXRecos.append((album, rating))
        

print()
print(sorted(userXRecos, key = itemgetter(1), reverse=False))





# sort list of tuples by highest rating to lowest rating.
# assign sorted list to varaible userXSortedRecos.
# Example: [('Phoenix', 4.0), ('Blues Traveler', 3.0), ('Slightly Stoopid', 2.5)]

# Code Chunk 5
userXSortedRecos = []
userXSortedRecos.append(sorted(userXRecos, key=itemgetter(1), reverse=True))

print()
print ("Recommendations for", userX)
print ("--------------------------")
print ()
print (userXSortedRecos)