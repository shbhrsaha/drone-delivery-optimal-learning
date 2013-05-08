"""
    This class contains the beliefs as the simulation is run
"""

class Simulation:
    
    meanMatrix = ""
    precisionMatrix = ""

    def __init__(self, simulationFile):
        """ Read the simulation file and instantiate this simulation """
        
        # read in file as matrix
        logging.info("Reading truth file")
        numberOfNodes = int(simulationFile.readline())
        meanListMatrix = nm.zeros((numberOfNodes,numberOfNodes))
        precisionListMatrix = nm.zeros((numberOfNodes,numberOfNodes))
        
        for line in simulationFile.readlines():
            
            columns = line.replace("\n","").split(" ")
            startNodeIndex = int(columns[0])
            endNodeIndex = int(columns[1])
            meanTravelTime = float(columns[2])
            precisionTravelTime = float(columns[3])
            
            meanListMatrix[startNodeIndex][endNodeIndex] = meanTravelTime
            precisionListMatrix[startNodeIndex][endNodeIndex] = precisionTravelTime
        
        # if you want to use Numpy matrices instead of arrays
        #self.meanMatrix = nm.matrix(meanListMatrix)
        #self.precisionMatrix = nm.matrix(precisionListMatrix)
        
        self.meanMatrix = meanListMatrix
        self.precisionMatrix = precisionListMatrix

        return

    def iterate(self, policyFunction):

        return