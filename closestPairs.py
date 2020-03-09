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

#helper method to sort by x coordinates
#p: a point
def sortByX(p):
    return (p.getX())

#helper method to sort by y coordinates
#p: a point
def sortByY(p):
    return (p.getY())

#define stripClosest method
#strip: a list of points, ?sorted by y coordinate? (not sure if I'm actually doing this...)
#size: size of strip
#d: minimum distance
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

#a method to compute the distance between two points
#p1: a point
#p2: a point
def distance(p1, p2):
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    dx2 = math.pow(dx, 2)
    dy2 = math.pow(dy, 2)
    return math.sqrt(dx2+dy2)
        

#define bruteForce method
#p: a list of points
#n: the number of points in p
def bruteForce(p, n):
    min = sys.float_info.max
    pSize = len(p)
    for i in range(0, n):
        for j in range(i+1, n):
            if(distance(p[i], p[j]) < min):
                min = distance(p[i], p[j])
    return min














#######################
# BEGIN "MAIN" METHOD #
#######################

# BEGIN READ FROM FILE AND FORMAT INTO A LIST #

# read the file
print("Opening file...")
theFile = open(sys.argv[1], "r")
print("Reading lines...")
rawLines = theFile.readlines()

# make an empty array to hold post processed list
print("Making empty arrays to hold post processed list...")
lines = [] 
points = []

# remove \n's
print("removing \\n's...")
for line in rawLines: 
    lines.append(line.replace("\n", "")) 

# save the number of points
print("Saving the number of points...")
numOfPoints = int(lines[0])

# remove number of points from the list -- make it easier later
print("Removing the number of points from lines list...")
lines.pop(0)

print("Create list containg Point objects...")
for line in lines:
    xy = line.split()
    x2 = xy
    y2 = xy
    y = float(y2.pop(1))
    x = float(x2.pop(0))
    myPoint = Point(x, y)
    points.append(myPoint)

print("Create xSortedPoints and ySortedPoints...")
xSortedPoints = sorted(points, key=sortByX)
ySortedPoints = sorted(points, key=sortByY)



print("##################\n# LIST OF POINTS #\n##################\n")
for point in points:
    print("x: "+str(point.getX()) + "\ty:" + str(point.getY()))
print("##################\n")

# start timer for execution time
print("Starting timer...")
start = t.time()



#####################################
# actually do the calculation here! #
#####################################
print("Calculating closest pairs...")
closestDistance = closestPairs(xSortedPoints, ySortedPoints, len(xSortedPoints))


# end timer for execution time
print("Stopping timer...")
end = t.time()

# calculate total execution time
print("Calculating execution time...")
totalTime = end - start

print("\n\n###########\n# RESULTS #\n###########")
print("Closest Distance: "+str(closestDistance))
print("Execution Time: "+str(totalTime))
print("Done!\n\n")
