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

nDivTwo = numOfPoints/2


# TODO: split up lines into X and Y parts,
# sort them according to pg 194

def closestPairs(p,q):
    if numOfPoints <= 3:
        #do brute force!
    else:
        # copy the first ⌈nDivTwo⌉ points of P to array Pl
        # copy the same ⌈nDivTwo⌉ points from Q to array Ql
        # copy the remaining ⌊nDivTwo⌋ points of P to array Pr
        # copy the same ⌊nDivTwo⌋ points from Q to array Qr
        # dl ← closestPairs(Pl, Ql)
        # dr ← closestPairs(Pr, Qr)
        # d ←min{dl, dr}
        # m ← P [⌈nDivTwo⌉ − 1].x
        # copy all the points of Q for which |x − m| < d into array S[0..num − 1] dminsq ← d2
        # for i ← 0 to num − 2 do
            # k←i+1
            # while k ≤ num − 1 and (S[k].y − S[i].y)2 < dminsq
                # dminsq ← min((S[k].x − S[i].x)2+ (S[k].y − S[i].y)2, dminsq)
                # k←k+1
    # return sqrt(dminsq)