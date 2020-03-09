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

    m = p[int((math.ceil(n/2))-1)].getX()

    s = [p for p in q  if abs(p.getX() - m) < d]
    numS = len(s)

    print(Dl)
    dminsq = pow(d, 2)

    for i in range(0, numS-2):
        k = i+1
        while (k<=numS-1) and (pow((s[k].getY()-s[i].getY()),2)<dminsq):
            dminsq = min((pow(s[k].getX() - s[i].getX(),2)+pow(s[k].getY() - s[i].getY(),2)),dminsq)
            k=k+1

    return math.sqrt(dminsq)