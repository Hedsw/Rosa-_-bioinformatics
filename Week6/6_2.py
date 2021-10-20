#! /usr/bin/python
import math

class xfinder:
    def __init__(self, L, c):
        self.state = []
        t = [x for x in L]
        t = sorted(t)
        self.high = t[-1]
        del t[-1]
        self.intList= [t[0]]
        for i in range(1,len(t)):
            if (t[i] != self.intList[-1]):
                self.intList.append(t[i])
        self.count = c
        self.slots = len(self.intList)
    def intSet(self):
        v = [0]
        offset = 0
        for i in range(len(self.state)):
            offset += self.state[i]
            v.append(self.intList[offset+i])
        v.append(self.high)
        return v

    def combinationsRemain(self):
        if (len(self.state) == 0):
            # handles first t ime
            self.state = [0 for i in range(self.count)]
            return True
        else:
            #nextCombination(self.state, len(self.intList))
            for i in range(len(self.state)-1,-1,-1):
                self.state[i] += 1
                if (sum(self.state) > self.slots - len(self.state)):
                    self.state[i] = 0
                else:
                    break
            
            return (sum(self.state) != 0)

def allPairsDist(L):
    #N = 0
    #N = N + 1
    dist = []
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            dist.append(L[j] - L[i])
    return dist

if __name__ == "__main__":
    Lists = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 9, 9, 10, 11, 12, 15]
    print(Lists)
    n = (math.sqrt(8 * len(Lists) + 1) + 1)/2
    if (int(n) != n):
        print("Invalid digest size")
    else:
        Lists = sorted(Lists)
        X = xfinder(Lists,int(n)-2)
        while (X.combinationsRemain()):
            distributedX = allPairsDist(X.intSet())
            distributedX.sort()
            if(distributedX == Lists):
                print("x = ", X.intSet())
        
    #print(N, " Iterations required")