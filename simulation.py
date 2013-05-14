"""
    This class contains the beliefs as the simulation is run
"""

import sys, simutils

import numpy as nm

class Simulation:
    
    numberOfNodes = 0
    meanMatrices = []
    covMatrices = []
    mappingDict = {}
    

    def __init__(self, priorsFile, covFile):
        """ Read the simulation file and instantiate this simulation """
        
        # read in priorsFile as matrix
        numberOfNodes = int(priorsFile.readline())
        self.numberOfNodes = numberOfNodes
        
        isFirstBlank = True
        for line in priorsFile.readlines():
            
            line = line.replace("\n","")
            
            if line == "":
                # start a new matrix
                if not isFirstBlank:
                    self.meanMatrices.append(meanMatrix)
                meanMatrix = nm.zeros((numberOfNodes,numberOfNodes))
                isFirstBlank = False
                continue
        
            line = line.split(" ")
            
            # add this line to the current matrix
            startNodeIndex = int(line[0])
            endNodeIndex = int(line[1])
            meanTravelTime = float(line[2])
        
            meanMatrix[startNodeIndex][endNodeIndex] = meanTravelTime
    
        # add the last matrix onto the list
        self.meanMatrices.append(meanMatrix)
    
        # read in the covariance file

        self.mappingDict = simutils.generateMappingDict(numberOfNodes)
                
        numberOfNodes = int(covFile.readline())
        if numberOfNodes != self.numberOfNodes:
            print "WARNING: number of nodes in covariance file does not match that in priorsFile"
        
        isFirstBlank = True
        for line in covFile.readlines():
            
            line = line.replace("\n","")
            
            if line == "":
                # start a new matrix
                if not isFirstBlank:
                    self.covMatrices.append(covMatrix)
                covMatrix = nm.zeros((numberOfNodes*numberOfNodes,numberOfNodes*numberOfNodes))
                isFirstBlank = False
                continue
            
            line = line.split(" ")
            
            # add this line to the current matrix
            startEdgeIndex = self.mappingDict[line[0] + " " + line[1]]
            endEdgeIndex = self.mappingDict[line[2] + " " + line[3]]
            cov = float(line[4])
            
            covMatrix[startEdgeIndex][endEdgeIndex] = cov
        
        # add the last matrix onto the list
        self.covMatrices.append(covMatrix)
        
        return


    def iterate(self, n, truth, simulation, policy):
        """ Simulates a single day of the simulation """
        
        tour = [0] # stores the nodes visited
        times = [] # stores the time to travel the edges
        nodesLeftToVisit = list(xrange(self.numberOfNodes))
        nodesLeftToVisit.pop(0)
        
        # repeat while we still have nodes left to visit
        while len(nodesLeftToVisit) > 0:
        
            current = tour[-1]
            
            # determine what type of day it is
            day_type = simutils.determineDayType(tour, times, meanMatrices)

            meanMatrix = self.meanMatrices[i]
            precisionMatrix = self.precisionMatrices[i]
            
            # prepare the alternatives to be fed into learning policy
            means_all = meanMatrix[current]
            precisions_all = precisionMatrix[current]
            
            # pop off all the means and precisions that are already in the tour
            means_left = [i for j, i in enumerate(means_all) if j not in tour]
            precisions_left = [i for j, i in enumerate(precisions_all) if j not in tour]

            # make the choice and add it to the tour
            choice_left = policy.make_choice(means_left, precisions_left, n)
            choice = nodesLeftToVisit[choice_left]
            tour.append(choice)
            nodesLeftToVisit.pop(choice_left)
        
            # measure the time it takes to travel this edge
            time = truth.measure(n,tour[-2],tour[-1])
            times.append(time)
        
        
        return

if __name__ == "__main__":

    priorsFile = open(sys.argv[1])
    covFile = open(sys.argv[2])
    
    simulation = Simulation(priorsFile, covFile)
    
    numberOfNodes = int(simulation.numberOfNodes)
    
    print "Successfully generated simulation object"
    print "Your priors file contains " + str(numberOfNodes) + " nodes"
    print "Here is what the various mean matrices look like: "
    
    for matrix in simulation.meanMatrices:
        print matrix
        print "=================================="

    print "Here is what the various covariance matrices look like: "
    
    for matrix in simulation.covMatrices:
        
        print matrix
        print "=================================="

    print "Unit testing complete."
