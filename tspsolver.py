"""
    This class solves the Traveling Salesman Problem
"""

import logging, math, random

import numpy as nm

logging.basicConfig(level=logging.INFO)

class TSPSolver:
    
    meanMatrix = ""
    
    def __init__(self, meanMatrix):
        
        self.meanMatrix = meanMatrix
        print meanMatrix
    
    def getTourLength(self, tour):
        """ Returns the time to travel the given tour on this instance's meanMatrix
        """
        
        size = len(tour)
        
        distance = 0
        for i in range(0,size - 1):
    
            j = tour[i]
            k = tour[i + 1]
            
            distance += meanMatrix[j][k]

        return distance
    
    def solveNearestNeighbor(self):
        """ Returns the fastest route using nearest neighbor heuristic
            
            Read in the next point, and add it to the current tour after the point to which it is closest. (If there is more than one point to which it is closest, insert it after the first such point you discover.)
        """
        meanMatrix = self.meanMatrix
        transposed = nm.transpose(meanMatrix)
        
        # derive number of buildings from matrix size
        size = int(math.sqrt(meanMatrix.size))
        
        # will store an ordered list of node ids to visit
        tour = []
        
        for i in range(0,size):
            
            print "Starting " + str(i)
        
            if len(tour) == 0:
                tour.append(i)
                continue
            
            # determine the index of the point in the current tour it is closest to
            distances = transposed[i]
            shortestStop = [100,100]
            for stop in tour:
                d = distances[stop]
                if d < shortestStop[1]:
                    shortestStop = (stop, d)
            closestNodeValue = shortestStop[0]
        
            # get and insert after that closest node
            closestNodeIndex = tour.index(closestNodeValue)
            tour.insert(closestNodeIndex + 1,i)
        
        return tour
    
    def solveSmallestIncrease(self, meanMatrix):
        """ Returns the time to travel the fastest route
            using smallest increase heuristic
            
            Read in the next point, and add it to the current tour after the point where it results in the least possible increase in the tour length. (If there is more than one point, insert it after the first such point you discover.)
        """
        
        # IMPLEMENTATION OPTIONAL
        
        return 0

if __name__ == "__main__":
    
    distanceRows = "0 7 8;7 0 13;6 7 0".split(";")
    distanceData = [map(int, x.split(" ")) for x in distanceRows]
    meanMatrix = nm.array(distanceData)

    tsp = TSPSolver(meanMatrix)
    tour = tsp.solveNearestNeighbor()
    print tour
    print tsp.getTourLength(tour)
