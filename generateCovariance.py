"""
Building codes:
Frist = 0, Nassau = 1, Whitman = 2, Forbes  3, Sherred = 4, Friend = 5, Lewis = 6

"""
import logging, math, random

import numpy as nm

nbuildings = 7;

for i in range (0,7):
    for j in range (0,7):
        for k in range (0,7):
            for l in range (0, 7):
                correlation = random.uniform(0.4, .99)
                if (i == k and j == l):
                    correlation = 1
                if (i == j or k == l):
                    correlation = 0
                covariance = correlation*5*10
                print i, j, k, l,  "%.2f" % round(covariance,2)
