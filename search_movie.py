# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:42:49 2018

@author: prabhat
"""

movie=open('movies.dat',"r")

 
def find(name):
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
            return m[0]
            break
        else:
            continue
    return -1   
    