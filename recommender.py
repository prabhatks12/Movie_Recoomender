# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 13:46:58 2018

@author: prabhat
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



#loading both the files
dataset = pd.read_csv("training_ratings.csv")



X=dataset.iloc[:,1].values
Y=dataset.iloc[:,2].values


#creating train and test set
from sklearn.cross_validation import train_test_split
trainX,testX,trainY,testY=train_test_split(X,Y,test_size=0.2)

# type trainX=..... writing only reshape wont work
trainX=trainX.reshape(-1,1)
trainY=trainY.reshape(-1,1)

testX=testX.reshape(-1,1)
testY=testY.reshape(-1,1)

#knn for classifications , ravael to remove warnings
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(trainX,trainY)

#u can use this too
"""
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(trainX,trainY.ravel())
"""

#simply predicting, for a movie say Avangers user1 can give rating =5 
#for the same movie , user2 can give 4 , user3=2..........
#we are finding the avg of ratings here 
#so if compare predicted avg value with the ratings given by different user, it will be a bad idea
# its like comparing avg=3 with 1,2,3,4,5 and saying less accuracy is obtained

pred = classifier.predict(testX)
pred=pred.reshape(-1,1)

#can see but according to above reasons accuracy will always be less
classifier.score(pred,testY,sample_weight=None)


#testing for user input 

movie=open('movies.dat',"r")
print("\n Enter a movie name")
name=input()
movieid=0
for n in movie :
        #splitting the dataset to get each individual attribute
        m=n.split('::')
        #movie id=m[0] movie_name=m[1]
        #converting everything tolower for string comparision
        moviename=str(m[1]).lower()  
        #print("Movie:",moviename)
        name=name.lower()
        if name in moviename:
            print("id",m[0])
            movieid=m[0]
            break
        else:
            continue

if movieid==-1:
    print("Not found")
else:    
    y=classifier.predict(movieid)
    y=int(y)
    print("Average Ratings : ",y)
    
    if y<=3:
        print("Not Good , Bad Ratings")
    elif y==4:
        print("Good Movie")
    else:
        print("Awesome Movie")
    
movie.close()




#    
#                                    OR
#





#if you want all the names of movie with ratings 5 , do this
good_movies=[]

#created an array of good movie_id 

print("All 5 rated movies id=")
for i in range(1,3952) :
    if classifier.predict(i)==5:
        print(i)
        good_movies.append(i)

print("And their names=")

lines=movie.readlines()
good_movies_name=[]

movie=open('movies.dat',"r")
for k in good_movies:
    k=int(k)
    for n in movie :
        #splitting the dataset to get each individual attribute
        m=n.split('::')
        m[0]=int(m[0])
        
        #movie id=m[0] movie_name=m[1]
        if k==m[0]:
            print(m[1])
            good_movies_name.append(m[1])
            break
        else:
            continue

#writing their names in external file
writefile=open("5rated_movies_name.txt","w")
for mname in good_movies_name:
    writefile.writelines(str(mname)+"\n")

writefile.close()        
movie.close()