"""
    This class contains the main function
    
    Usage: python main.py [simulation file] [truth file] [iterations] [policy]
    
"""
import sys, logging




logging.basicConfig(level=logging.INFO)

def main():

    # read in data from command line
    logging.info("Reading simulation parameters")

    if len(sys.argv) == 5:
        SIMULATION_FILE_PATH = sys.argv[1]
        TRUTH_FILE_PATH = sys.argv[2]
        NUMBER_OF_ITERATIONS = sys.argv[3]
        POLICY_NAME = sys.argv[4]
    else:
        logging.error("Invalid parameters: python main.py [simulation file] [truth file] [iterations] [policy]")
        sys.exit()

    # create truth, simulation, and policy objects
    logging.info("Loading truth, simulation, and policy")
    simulationFile = open(SIMULATION_FILE_PATH)
    truthFile = open(TRUTH_FILE_PATH)

    truth = Truth(truthFile)
    simulation = Simulation(simulationFile)
    policy = Policy(POLICY_NAME)

if __name__ == "__main__":
    main()