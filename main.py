"""
    This class contains the main function
    
    Usage: python main.py [simulation file] [truth file] [iterations] [policy]
    
"""
import sys, logging
from truth import *
from policy import *
from simulation import *

logging.basicConfig(level=logging.INFO)

def main():

    # read in data from command line
    logging.info("Reading simulation parameters")

    if len(sys.argv) == 7:
        SIMULATION_FILE_PATH = sys.argv[1]
        COV_FILE = sys.argv[2]
        TRUTH_FILE_PATH = sys.argv[3]
        DAY_FILE_PATH = sys.argv[4]
        NUMBER_OF_ITERATIONS = int(sys.argv[5])
        POLICY_NAME = sys.argv[6]
    else:
        logging.error("Invalid parameters")
        sys.exit()

    # create truth, simulation, and policy objects
    priorsFile = open(SIMULATION_FILE_PATH)
    covFile = open(COV_FILE)
    truthFile = open(TRUTH_FILE_PATH)
    dayFile = open(DAY_FILE_PATH)

    truth = Truth(truthFile, dayFile)
    simulation = Simulation(priorsFile, covFile)
    policy = Policy(POLICY_NAME )

    totalDistance = 0
    for n in range(1,NUMBER_OF_ITERATIONS):

        totalDistance = simulation.iterate(n, truth, simulation, policy)

    averageTravelTime = totalDistance/float(NUMBER_OF_ITERATIONS)

    print "Average Travel Time: " + str(averageTravelTime)

if __name__ == "__main__":
    main()