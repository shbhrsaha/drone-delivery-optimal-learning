"""
Building codes:
Frist = 0, Nassau = 1, Whitman = 2, Forbes  3, Sherred = 4, Friend = 5, Lewis = 6

"""
import logging, math, random

import numpy as nm

nbuildings = 7;

print nbuildings

print

edgebelief = {};
covariancematrix = [[0 for x in xrange(49*49)] for x in xrange(5)]

for i in range (0,nbuildings):
    for j in range (0,nbuildings):
        edgebelief[str(i)+str(j)] = random.randint(5,15);
        if (i == j):
            edgebelief[str(i)+str(j)] = 0
counter = 0;
for i in range (0,nbuildings):
    for j in range (0,nbuildings):
        for k in range (0,nbuildings):
            for l in range (0, nbuildings):
                correlation = random.uniform(0.4, .99)
                if (i == k and j == l):
                    correlation = 1
                if (i == j or k == l):
                    correlation = 0
                covariance = correlation*edgebelief[str(i)+str(j)]*edgebelief[str(k)+str(l)]
                covariancematrix[0][counter] = i
                covariancematrix[1][counter] = j
                covariancematrix[2][counter] = k
                covariancematrix[3][counter] = l
                covariancematrix[4][counter] = covariance
                counter += 1
for i in range (0, 49*49):
    print covariancematrix[0][i], covariancematrix[1][i], covariancematrix[2][i], covariancematrix[3][i],  "%.2f" % round(covariancematrix[4][i],2)
                
                
