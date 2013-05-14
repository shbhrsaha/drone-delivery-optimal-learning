
import sys, itertools

# truth file containing just the medium truth
truthFile = open(sys.argv[1])

# prior file containing just the medium truth
priorFile = open(sys.argv[2])

# this dictionary will store all the data
data = {}

n = int(truthFile.readline())
truthFile.readline()
priorFile.readline()
priorFile.readline()

# read in the data
for line in truthFile.readlines():

    lineData = line.replace("\n","").split(" ")

    start = lineData[0]
    end = lineData[1]
    time = float(lineData[2])
    noise = float(lineData[3])

    data[start + " " + end] = (time,noise)

# generate routes, store in list
alternatives = [x for x in range(0,n)]
routes = itertools.permutations(alternatives)


# generate and print route travel times
meansToPrint = []
noiseToPrint = []

index = 0
for route in routes:
    
    # only take ones that start at Frist
    if route[0] == 0:

        totalTime = 0
        totalNoise = 0
        for i in range(0,n - 1):
            totalTime += data[str(route[i]) + " " + str(route[i + 1])][0]
            totalNoise += data[str(route[i]) + " " + str(route[i + 1])][1]
        
        meansToPrint.append(str(totalTime))
        noiseToPrint.append(str(round(totalNoise/float(n - 1),2)))

        index += 1

print ";".join(meansToPrint)
print ";".join(noiseToPrint)

# ======================================================

data = {}

# read in the data
for line in priorFile.readlines():
    
    lineData = line.replace("\n","").split(" ")
    
    start = lineData[0]
    end = lineData[1]
    time = float(lineData[2])
    
    data[start + " " + end] = time

meansToPrint = []

alternatives = [x for x in range(0,n)]
routes = itertools.permutations(alternatives)

for route in routes:

    # only take ones that start at Frist
    if route[0] == 0:
        
        totalTime = 0
        for i in range(0,n - 1):
            totalTime += data[str(route[i]) + " " + str(route[i + 1])]
        
        meansToPrint.append(str(totalTime))
    
        index += 1

print ";".join(meansToPrint)