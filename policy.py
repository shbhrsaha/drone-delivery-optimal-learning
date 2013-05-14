"""
    This file contains the policies used in the simulation
"""

import sys, logging, random, math
import simutils

logging.basicConfig(level=logging.INFO)

class Policy:

    VALID_POLICY_NAMES = ["epsilon-greedy","boltzmann-exploration","interval-estimation","knowledge-gradient"]

    policy_name = ""
    
    # tunable parameters
    c = 0.5
    rho = 0.5
    zalpha = 0.1
    

    def __init__(self, policy_name):
        """ Accepts the policy_name and returns false if policy_name invalid"""

        if policy_name in self.VALID_POLICY_NAMES:
            self.policy_name = policy_name
            return
        else:
            return false

    def make_choice(self, means, precisions, n):
        """ Returns the index of the alternative to choose given a list of means and precisions """
        
        means = [-1*x for x in means]
        
        if len(means) == 1:
            return 0

        # EPSILON-GREEDY
        if self.policy_name == "epsilon-greedy":
            
            c = self.c
            
            epsilon = c/float(n)
            
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
            
            rho = self.rho
            
            size = len(means)
            weights = []
            for i in range(0, size):
                other_means = [x for index,x in enumerate(means) if index != i]
                denominator_terms = [math.exp(rho*x) for x in other_means]
                denominator = sum(denominator_terms)
                p = math.exp(rho*means[i])/float(denominator)
                weights.append(p)
            
            return simutils.weighted_choice(means,weights)


        # INTERVAL ESTIMATION
        elif self.policy_name == "interval-estimation":
            
            zalpha = self.zalpha
            
            scores = [x + zalpha*(1/math.sqrt(y)) for x,y in zip(means,precisions)]
            
            # return index of the max score
            return max(xrange(len(scores)),key=scores.__getitem__)

        # KNOWLEDGE GRADIENT WITH CORRELATED BELIEFS -- not implemented yet... see MATLAB
        elif self.policy_name == "knowledge-gradient":

            return

            """
            theta_n = [x for x in means]
            max_x = []
            sigma_n = [1/math.sqrt(x) for x in precisions]
            sigmatilde_n = []
            zeta = []
            normcdf = []
            normdensity = []
            f_z = []
            KGindex = []
            
            # return max(xrange(len(KGindex)),key=KGindex.__getitem__)
            return False
            """
                
        else:

            return False
