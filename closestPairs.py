import time as t
import sys
import math

#define a point
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

#define closestPairs method
#p: x sorted array of points
#q: y sorted array of points
def closestPairs(p,q):
    n = len(p)
    nDivTwoCeil = math.ceil(n/2)
    nDivTwoFloor = math.floor(n/2)
    pl = []
    ql = []
    if numOfPoints <= 3:
        print('inIf')
        #bruteForceIt
    else:
        print('inElse')
        # copy the first ⌈nDivTwo⌉ points of P to array Pl
        for points in range(nDivTwoCeil):
            pl.append(points)

        # copy the same ⌈nDivTwo⌉ points from Q to array Ql
        for points in range(nDivTwoCeil):
            ql.append(points)

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

#define bruteForce method
def bruteForce(p,q):
    print("doBruteForce")
    #doBruteForce

# read the file
theFile = open(sys.argv[1], "r")
rawLines = theFile.readlines()

# make an empty array to hold post processed list
lines = [] 
points = []

# remove \n's
for line in rawLines: 
    lines.append(line.replace("\n", "")) 

# save the number of points
numOfPoints = int(lines[0])

# remove number of points from the array -- make it easier later
lines.pop(0)

for line in lines:
    xy = line.split()
    x2 = xy
    y2 = xy
    y = float(y2.pop(1))
    x = float(x2.pop(0))
    myPoint = Point(x, y)
    points.append(myPoint)

def sortByX(p):
    return (p.getX())

def sortByY(p):
    return (p.getY())

xSortedPoints = sorted(points, key=sortByX)
ySortedPoints = sorted(points, key=sortByY)



###################################
# BEGIN THE CLOSEST PAIRS PROBLEM #
###################################

#closestPairs(xSortedPoints, ySortedPoints)