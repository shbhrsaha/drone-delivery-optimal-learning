"""
    This class contains the true edge travel times for the simulations
"""

import logging, math, random

import numpy as nm

logging.basicConfig(level=logging.INFO)

class Truth:
    
    meanMatrix = ""
    noiseMatrix = ""

    def __init__(self, truthFile):
        """ Read the truth file and instantiate this instance """
        
        # read in file as matrix
        logging.info("Reading truth file")
        numberOfNodes = int(truthFile.readline())
        meanListMatrix = nm.zeros((numberOfNodes,numberOfNodes))
        noiseListMatrix = nm.zeros((numberOfNodes,numberOfNodes))
        
        for line in truthFile.readlines():
        
            columns = line.replace("\n","").split(" ")
            startNodeIndex = int(columns[0])
            endNodeIndex = int(columns[1])
            meanTravelTime = float(columns[2])
            noiseTravelTime = float(columns[3])
        
            meanListMatrix[startNodeIndex][endNodeIndex] = meanTravelTime
            noiseListMatrix[startNodeIndex][endNodeIndex] = noiseTravelTime
        
        # if you want to use Numpy matrices instead of arrays
        #self.meanMatrix = nm.matrix(meanListMatrix)
        #self.noiseMatrix = nm.matrix(noiseListMatrix)
        
        self.meanMatrix = meanListMatrix
        self.noiseMatrix = noiseListMatrix
                
        return

    def measure(self, startNodeIndex, endNodeIndex):
        """ Returns a measured value from the truth.
            
            Assumes truth is normally distributed
        """
        
        mean = self.meanMatrix[startNodeIndex][endNodeIndex]
        noise = self.noiseMatrix[startNodeIndex][endNodeIndex]

        # ensure measurement is a positive number
        x = -1
        while x < 0:
            x = random.gauss(mean, math.sqrt(noise))

        return x