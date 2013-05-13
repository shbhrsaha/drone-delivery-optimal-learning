"""
Building codes:
Frist = 1, Nassau = 2, Whitman = 3, Fobes  4, Sherred = 5, Friend = 6, Lewis = 7

"""
import logging, math, random

import numpy as nm

Map = {'1': (0,0),'2': (-1,4), '3': (-2,-2),'4' : (-6,-2),'5': (3,2), '6': (3,3.5), '7': (3, -2)};
distancePrior = [[0 for x in xrange(7)] for x in xrange(7)];
for i in range(1, 8):
    for j in range(1, 8):
        point1 = nm.asarray(Map[str(i)])
        point2 = nm.asarray(Map[str(j)])
        dist = nm.linalg.norm(point1-point2)
        distancePrior[i-1][j-1] = dist
nm.set_printoptions(precision=3)
for i in range(0, 7):
    for j in range(0, 7):
        print (distancePrior[i][j]),
    print;
    
    