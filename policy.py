"""
    This file contains the policies used in the simulation
"""

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

    def make_decision(self, means, precisions):
        """ Returns the index of the alternative to choose given a list of means and precisions """

        if self.policy_name == "epsilon-greedy":

            return True

        elif self.policy_name == "interval-estimation":

            return True

        elif self.policy_name == "knowledge-gradient":

            return True

        else:

            return false
