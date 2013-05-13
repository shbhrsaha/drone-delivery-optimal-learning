"""
Building codes:
Frist = 0, Nassau = 1, Whitman = 2, Forbes  3, Sherred = 4, Friend = 5, Lewis = 6

"""
import logging, math, random

import numpy as nm

nbuildings = 7;

Map = {'0': (0,0),'1': (-1,4), '2': (-2,-2),'3' : (-6,-2),'4': (3,2), '5': (3,3.5), '6': (3, -2)};

for i in range(0, nbuildings):
    for j in range(0, nbuildings):
        point1 = nm.asarray(Map[str(i)])
        point2 = nm.asarray(Map[str(j)])
        slowdist = nm.linalg.norm(point1-point2)*2.5
        if (slowdist != 0):
            slowdist += 4 
        print i, j, "%.2f" % round(slowdist,2)
        
for i in range(0, nbuildings):
    for j in range(0, nbuildings):
        point1 = nm.asarray(Map[str(i)])
        point2 = nm.asarray(Map[str(j)])
        mediumdist = nm.linalg.norm(point1-point2)*2.5
        print i, j, "%.2f" % round(mediumdist,2)
        
for i in range(0, nbuildings):
    for j in range(0, nbuildings):
        point1 = nm.asarray(Map[str(i)])
        point2 = nm.asarray(Map[str(j)])
        fastdist = nm.linalg.norm(point1-point2)*2.5
        if (fastdist != 0):
            fastdist -= 2 
        print i, j, "%.2f" % round(fastdist,2)
        
    
    
