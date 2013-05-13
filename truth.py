"""
    This class contains the true edge travel times for the simulations
"""

import logging, math, random

import numpy as nm

logging.basicConfig(level=logging.INFO)

class Truth:
    
    meanMatrices = ""
    noiseMatrices = ""

    def __init__(self, truthFile):
        """ Read the truth file and instantiate this instance """
        
        # read in file as matrix
        logging.info("Reading truth file")
        numberOfNodes = int(truthFile.readline())
        
        for line in truthFile.readlines():
        
            line = line.replace("\n","")
            
            if line == "":
                # start a new matrix
                if len(meanMatrices) != 0:
                    self.meanMatrices.append(meanMatrix)
                    self.noiseMatrices.append(noiseMatrix)
                meanMatrix = nm.zeros((numberOfNodes,numberOfNodes))
                noiseMatrix = nm.zeros((numberOfNodes,numberOfNodes))
                continue
    
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

        return

    def measure(self, matrixIndex, startNodeIndex, endNodeIndex):
        """ Returns a measured value from the truth.
            
            Assumes truth is normally distributed
        """
        
        mean = self.meanMatrices[matrixIndex][startNodeIndex][endNodeIndex]
        noise = self.noiseMatrices[matrixIndex][startNodeIndex][endNodeIndex]

        # ensure measurement is a positive number
        x = -1
        while x < 0:
            x = random.gauss(mean, math.sqrt(noise))

        return x