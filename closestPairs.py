import time as t
import sys
import math

infinity = float('inf')

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
    if n <= 3:
        return bruteForce(p)
    Pl = p[:n//2]
    Pr = p[n//2:]

    Ql = q[:n//2]
    Qr = q[n//2:]

    Dl = closestPairs(Pl, Ql)
    Dr = closestPairs(Pr, Qr)

    d = min(Dl, Dr)

    m = p[(math.ceil(n/2))-1].getX()

    s = [p for p in q  if abs(p - m) < d]
    numS = len(s)

    dminsq = pow(d, 2)

    for i in range(0, numS-2):
        k = i+1
        while (k<=numS-1) and (pow((s[k].getY()-s[i].getY()),2)<dminsq):
            dminsq = min((pow(s[k].getX() - s[i].getX(),2)+pow(s[k].getY() - s[i].getY(),2)),dminsq)
            k=k+1
    return math.sqrt(dminsq)


        

#define bruteForce method
def bruteForce(p):
    numPoints = len(p)
    if numPoints < 2:
        return null
    

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

closestPairs(xSortedPoints, ySortedPoints)