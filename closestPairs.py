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

    def __str__(self):
        return "Point(%s,%s)"%(self.x,self.y)

def stripClosest(strip, size, d):
    min = d

    for i in range(0, size):
        j = i+1
        while (j<size and ((strip[j].y - strip[i].y)<min)):
            if(distance(strip[i], strip[j]) < min):
                min = distance(strip[i], strip[j])
            j+=1
    
    return min


#define closestPairs method
#p: x sorted array of points
#q: y sorted array of points
def closestPairs(Px, Py, n):

    if n<=3:
        return bruteForce(Px, n)

    mid = n//2
    midpoint = Px[mid]

    Pyl = Py[:n//2]
    Pyr = Py[n//2:]

    dl = closestPairs(Px, Pyl, mid)
    dr = closestPairs(Px, Pyr, n-mid)

    d = min(dl, dr)
   
    strip = [Point] * n

    j = 0
   
    for i in range(0, n):
        if(abs(Py[i].getX() - midpoint.getX()) < d):
            strip[j] = Py[i]
            j = j + 1
    
    return min(d, stripClosest(strip, j, d))


def distance(p1, p2):
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    dx2 = math.pow(dx, 2)
    dy2 = math.pow(dy, 2)
    return math.sqrt(dx2+dy2)
        

#define bruteForce method
def bruteForce(p, n):
    min = sys.float_info.max
    pSize = len(p)
    for i in range(0, n):
        for j in range(i+1, n):
            if(distance(p[i], p[j]) < min):
                min = distance(p[i], p[j])
    return min


#####################
# BEGIN MAIN METHOD #
#####################

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

print(closestPairs(xSortedPoints, ySortedPoints, len(xSortedPoints)))