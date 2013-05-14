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

def newCovariance(oldCovariance, observed):

    return True

# CONVERT COVARIANCE MATRIX TO VARIANCE
# =====================================

def readVariance():

    return True

# GENERATE SOME SORT OF MAPPING DICTIONARY
# TO GO FROM EDGE IDENTIFIERS TO INDEX IN COV MATRIX
# ==================================================

def generateMappingDict(n):

    mappingDict = {}
    
    nextAvailableIndex = 0
    
    for i in range(0,n):
        for j in range(0,n):
            code = str(i) + " " + str(j)
            mappingDict[code] = nextAvailableIndex
            nextAvailableIndex += 1

    return mappingDict

# DETERMINE DAY TYPE
# ==================

def determineDayType(tour, times, meanMatrices):

    number_of_types = len(meanMatrices)

    scores = []
    for i in range(0, number_of_types):
        
        pastTimes = [meanMatrices[i][j][j + 1] for j in range(0,len(tour) - 1)]
        terms = [obs - past for obs,past in zip(times,pastTimes)]
        scores[i] = 1/float(sum(terms))

    return max(xrange(len(scores)),key=scores.__getitem__)

# UNIT TESTING
# ============

if __name__ == "__main__":
    
    mappingDict = generateMappingDict(3)
    
    print mappingDict