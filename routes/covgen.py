
import sys, itertools, logging

import numpy as nm

logging.basicConfig(level=logging.INFO)

n = 7

alternatives = [x for x in range(0,n)]
routes1 = list(itertools.permutations(alternatives))

routes1 = [x for x in routes1 if x[0] == 0]
routes2 = routes1

matrix = nm.zeros((len(routes1),len(routes1)))

covLookup = [0, 0.18, 0.34, 0.5, 0.66, 0.83, 1.0]

counterBig = 0
for r in routes1:
    
    edges1 = []
    for i in range(0,len(covLookup) - 1):
        edges1.append(str(r[i]) + " " + str(r[i + 1]))

    counterSmall = 0
    for s in routes2:

        edges2 = []
        for i in range(0,len(covLookup) - 1):
            edges2.append(str(s[i]) + " " + str(s[i + 1]))
        
        score = len(list(set(edges1).intersection(edges2)))
        matrix[counterBig][counterSmall] = covLookup[score]
    
        counterSmall += 1

    counterBig += 1

    logging.info(counterBig)

sys.stdout.write("[")

for row in matrix:

    sys.stdout.write("[")
    for item in row:
        sys.stdout.write(str(round(item,2)) + ",")
    sys.stdout.write("];")

sys.stdout.write("]")