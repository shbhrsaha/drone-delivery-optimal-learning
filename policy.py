"""
    This file contains the policies used in the simulation
"""

import sys, logging, random, math
import simutils

logging.basicConfig(level=logging.INFO)

class Policy:

    VALID_POLICY_NAMES = ["epsilon-greedy","boltzmann-exploration","interval-estimation","knowledge-gradient"]

    policy_name = ""


    def __init__(self, policy_name):
        """ Accepts the policy_name and returns false if policy_name invalid"""

        if policy_name in self.VALID_POLICY_NAMES:
            self.policy_name = policy_name
            return
        else:
            return false

    def make_decision(self, means, precisions, epsilon = False, rho = False):
        """ Returns the index of the alternative to choose given a list of means and precisions """

        # EPSILON-GREEDY
        if self.policy_name == "epsilon-greedy":

            # make sure epsilon is defined
            if not epsilon:
                logging.error("Invalid parameters: You must provide an epsilon at each iteration of epsilon-greedy policy")
                sys.exit()
            
            # toss this epsilon-weighted coin to see if we'll explore or exploit
            uniform_sampling = random.random()
            if uniform_sampling < epsilon:
                # explore
                choice = random.randrange(0,len(means),1)
            else:
                # exploit
                choice = max(xrange(len(means)),key=means.__getitem__)
                    
            return choice
    
        # BOLTZMANN-EXPLORATION
        elif self.policy_name == "boltzmann-exploration":
            
            # make sure epsilon is defined
            if not rho:
                logging.error("Invalid parameters: You must provide rho at each iteration of Boltzmann-exploration policy")
                sys.exit()
    
            size = len(means)
            weights = []
            for i in range(0, size):
                other_means = [x for index,x in enumerate(means) if index != i]
                denominator_terms = [math.exp(rho*x) for x in other_means]
                denominator = sum(denominator_terms)
                p = math.exp(rho*means[i])/float(denominator)
            weights.append(p)

            return simutils.weighted_choice(means,weights)

        elif self.policy_name == "interval-estimation":
            
            
            
            return True

        elif self.policy_name == "knowledge-gradient":

            return True

        else:

            return False
