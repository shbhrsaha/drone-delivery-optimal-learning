"""
    Useful functions
"""

import random
import bisect
import collections

# WEIGHTED PROBABILITY FUNCTIONS
# ==============================
def cdf(weights):
    total=sum(weights)
    result=[]
    cumsum=0
    for w in weights:
        cumsum+=w
        result.append(cumsum/total)
    return result

def weighted_choice(population,weights):
    """
        weights=[0.3,0.4,0.3]
        weighted_choice(population,weights) # returns index of that choice
    """
    
    assert len(population) == len(weights)
    cdf_vals=cdf(weights)
    x=random.random()
    idx=bisect.bisect(cdf_vals,x)
    return idx


# CORRELATED BELIEFS UPDATING EQUATIONS
# =====================================

def newMean(oldMean, observed):

    return True

