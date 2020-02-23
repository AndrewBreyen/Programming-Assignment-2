import time as t
import sys

# read the file
theFile = open(sys.argv[1], "r")
rawLines = theFile.readlines()

# make an empty array to hold post processed list
lines = [] 

# remove \n's
for line in rawLines: 
    lines.append(line.replace("\n", "")) 

# save the number of points
numOfPoints = lines[0]

# remove number of points from the array -- make it easier later
lines.pop(0)




def closestPairs(p,q):
    print("yeet")