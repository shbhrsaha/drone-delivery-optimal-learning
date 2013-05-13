"""
    This class contains the beliefs as the simulation is run
"""

class Simulation:
    
    numberOfNodes = 0
    meanMatrices = ""
    precisionMatrices = ""

    def __init__(self, simulationFile):
        """ Read the simulation file and instantiate this simulation """
        
        # read in file as matrix
        logging.info("Reading simulation file")
        self.numberOfNodes = int(simulationFile.readline())

        meanListMatrix = nm.zeros((numberOfNodes,numberOfNodes))
        precisionListMatrix = nm.zeros((numberOfNodes,numberOfNodes))
        
        for line in truthFile.readlines():
            
            line = line.replace("\n","")
            
            if line == "":
                # start a new matrix
                if len(meanMatrices) != 0:
                    self.meanMatrices.append(meanMatrix)
                    self.precisionMatrices.append(precisionMatrix)
                meanMatrix = nm.zeros((numberOfNodes,numberOfNodes))
                noiseMatrix = nm.zeros((numberOfNodes,numberOfNodes))
                continue
            
            # add this line to the current matrix
            startNodeIndex = int(line[0])
            endNodeIndex = int(line[1])
            meanTravelTime = float(line[2])
            noiseTravelTime = float(line[3])
            
            meanMatrix[startNodeIndex][endNodeIndex] = meanTravelTime
            precisionMatrix[startNodeIndex][endNodeIndex] = noiseTravelTime
        
        # add the last matrix onto the list
        self.meanMatrices.append(meanMatrix)
        self.precisionMatrices.append(precisionMatrix)
        
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
            # TODO: WRITE THIS LOGIC
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