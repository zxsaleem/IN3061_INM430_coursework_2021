#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:31:14 2022

@author: macair
"""
import sys
import csv
print('Hello, World!')
f = open("/Users/macair/Documents/week1 python/TB_burden_countries_2014-09-29.csv")
count=0
for row in csv.reader(f):
    count+=1
    
print(count)


###################################################


#%%
f = open("/Users/macair/Documents/week1 python/TB_burden_countries_2014-09-29.csv")
count=0 
flag=0
for row in csv.reader(f):

    
    try: 
        count+=1
        flag=int(row[6])
       
    except Exception:
        next (f)
    
print(flag)
average= flag/count
print(average)

    #%%

f = open("/Users/macair/Documents/week1 python/TB_burden_countries_2014-09-29.csv")
count=0 
flag=0
for row in csv.reader(f):
    if row [5]== "1990" :
        try:
            count+=1
            flag=int(row[6])
           
        except Exception:
            next (f)
    
print("sum: ",flag)
average= flag/count
print("average: ",average)


f = open("/Users/macair/Documents/week1 python/TB_burden_countries_2014-09-29.csv")
count=0 
flag=0
for row in csv.reader(f):
    if row [5]== "2011" :
        try:
            count+=1
            flag=int(row[6])
           
        except Exception:
            next (f)
    
print("sum2: ",flag)
average= flag/count
print("average2: ",average)

import numpy as np

np.arange(5,15,1)
a= np.arange(5,15,1)
print (a)

np.arange(0,23,7)
b= np.arange(0,23,7)
print (b)

c=np.random.uniform (-1,1,[5,5])
print (c)

import matplotlib.pyplot as plt

d=plt.hist (c,5)
(d,np.ones_like) 
end= np.random.randint(1,10,10)
end2 = np.random.randint(10,20,10)
flag1=0 
print (end)
for i in range (0,10) : 
    
    ec=end[i]- end2[i] 
    flag1=ec+flag1
euc=np.sqrt(np.square(flag1)) 
print (euc)


    

