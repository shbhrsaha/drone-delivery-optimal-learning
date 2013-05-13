"""
    This class contains the true edge travel times for the simulations
"""
import sys
import logging, math, random

import numpy as nm

logging.basicConfig(level=logging.INFO)

class Truth:
    
    meanMatrices = []
    noiseMatrices = []
    numberOfNodes = 0
    days = []

    def __init__(self, truthFile, dayFile):
        """ Read the truth file and instantiate this instance """
        
        # read in file as matrix
        numberOfNodes = int(truthFile.readline())
        self.numberOfNodes = numberOfNodes
        
        isFirstBlank = True
        for line in truthFile.readlines():
        
            line = line.replace("\n","")
            
            if line == "":
                # start a new matrix
                if not isFirstBlank:
                    self.meanMatrices.append(meanMatrix)
                    self.noiseMatrices.append(noiseMatrix)
                meanMatrix = nm.zeros((numberOfNodes,numberOfNodes))
                noiseMatrix = nm.zeros((numberOfNodes,numberOfNodes))
                isFirstBlank = False
                continue
    
            line = line.split(" ")
            
            # add this line to the current matrix
            startNodeIndex = int(line[0])
            endNodeIndex = int(line[1])
            meanTravelTime = float(line[2])
            noiseTravelTime = float(line[3])
            
            meanMatrix[startNodeIndex][endNodeIndex] = meanTravelTime
            noiseMatrix[startNodeIndex][endNodeIndex] = noiseTravelTime
        
        # add the last matrix onto the list
        self.meanMatrices.append(meanMatrix)
        self.noiseMatrices.append(noiseMatrix)

        # read in the day file
        dayFile.readline() # skip the first line, contains the number of days
        self.days = [int(line.replace("\n","")) for line in dayFile.readlines()]
        
        return

    def measure(self, n, startNodeIndex, endNodeIndex):
        """ Returns a measured value from the truth.
            
            Assumes truth is normally distributed
        """
        
        matrixIndex = self.days[n]
        
        mean = self.meanMatrices[matrixIndex][startNodeIndex][endNodeIndex]
        noise = self.noiseMatrices[matrixIndex][startNodeIndex][endNodeIndex]

        # ensure measurement is a positive number
        x = -1
        while x < 0:
            x = random.gauss(mean, math.sqrt(noise))

        return x

if __name__ == "__main__":
    """ Read in the truth and day file and output the matrices """

    truthFile = open(sys.argv[1])
    dayFile = open(sys.argv[2])

    truth = Truth(truthFile, dayFile)

    numberOfNodes = int(truth.numberOfNodes)
    
    print "Successfully generated truth object"
    print "Your truth file contains " + str(numberOfNodes) + " nodes"
    print "Your day file indicates this simulation will run over " + str(len(truth.days)) + " days with " + str(len(truth.meanMatrices)) + " types"
    print "Here is a sample of the types in the first few days: " + str(truth.days[:5])
    print "Here is what the various mean matrices look like: "
    
    for matrix in truth.meanMatrices:
        print matrix
    
    print "Here is what the various noise matrices look like: "

    for matrix in truth.noiseMatrices:
        print matrix


    print "Let's make some measurements: "
    
    for i in range(0,10):
        
        print "Day type " + str(truth.days[i]) + ": " + str(truth.measure(i, random.randint(0,numberOfNodes - 1), random.randint(0,numberOfNodes - 1)))
    
    print "Unit testing complete."