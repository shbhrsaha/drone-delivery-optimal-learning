"""
Building codes:
Frist = 0, Nassau = 1, Whitman = 2, Forbes  3, Sherred = 4, Friend = 5, Lewis = 6

"""
import logging, math, random

import numpy as nm

nbuildings = 7;

print nbuildings

print

Map = {'0': (0,0),'1': (-1,4), '2': (-2,-2),'3' : (-6,-2),'4': (3,2), '5': (3,3.5), '6': (3, -2)};

for i in range(0, nbuildings):
    for j in range(0, nbuildings):
        point1 = nm.asarray(Map[str(i)])
        point2 = nm.asarray(Map[str(j)])
        slowtruth = nm.linalg.norm(point1-point2)*2.5
        if (slowtruth != 0):
            slowtruth += random.gauss(4, 10)
            if (slowtruth < 0):
                slowtruth = math.fabs(slowtruth);
        variance = random.gauss(8, 15);
        if (variance < 0):
            variance = math.fabs(variance);
        if (slowtruth == 0):
            variance = 0;
        print i, j, "%.2f" % round(slowtruth,2), "%.2f" % round(variance,2)
        
print
        
for i in range(0, nbuildings):
    for j in range(0, nbuildings):
        point1 = nm.asarray(Map[str(i)])
        point2 = nm.asarray(Map[str(j)])
        mediumtruth = nm.linalg.norm(point1-point2)*2.5
        if (mediumtruth != 0):
            mediumtruth += random.gauss(0, 10)
            if (mediumtruth < 0):
                mediumtruth = math.fabs(mediumtruth);
        variance = random.gauss(8, 15);
        if (variance < 0):
            variance = math.fabs(variance);
        if (mediumtruth == 0):
            variance = 0;
        print i, j, "%.2f" % round(mediumtruth,2), "%.2f" % round(variance,2)

print
        
for i in range(0, nbuildings):
    for j in range(0, nbuildings):
        point1 = nm.asarray(Map[str(i)])
        point2 = nm.asarray(Map[str(j)])
        fasttruth = nm.linalg.norm(point1-point2)*2.5
        if (fasttruth != 0):
            fasttruth -= random.gauss(2, 10)
            if (fasttruth < 0):
                fasttruth = math.fabs(fasttruth);
        variance = random.gauss(8, 15);
        if (variance < 0):
            variance = math.fabs(variance);
        if (fasttruth == 0):
            variance = 0;
        print i, j, "%.2f" % round(fasttruth,2), "%.2f" % round(variance,2)
    
    
