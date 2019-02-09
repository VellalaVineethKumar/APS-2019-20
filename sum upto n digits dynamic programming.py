# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 09:32:37 2019

@author: lenovo

ways to get sum=15 using 3,5,10
"""
import timeit

start = timeit.default_timer()

#Your statements here


a = []

for i in range(16):
    a.append(0)
numb=3,5,10
a[0]=1

num=0
#sum is 15 hence poupulate the array upro 15 indices

    # we will have two pointers pointing to the array indices
for val in numb:
    for i in range(16):
        for j in range(val,16,1):   
                if(j-i==val):
                    a[j]=a[j]+a[i]                   
                
     
print(a)
stop = timeit.default_timer()

print('Time: ', stop - start)  