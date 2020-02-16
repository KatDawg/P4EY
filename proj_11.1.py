#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  16 2020

@author: Brian Pacheco
"""
import re
fh = open('regex_sum_359520.txt')
#Create empty List
numList = []
total = 0
for line in fh:
    #Strip each line to evaluate
    line = line.rstrip()
    #Find all numbers in line
    stuff = re.findall('[0-9]+', line)
    #Convert each number in stuff list to a float and
    #add to NumList
    for item in stuff:
        numList.append(float(item))
#Sum of numbers found
total = sum(numList)
print(total)
