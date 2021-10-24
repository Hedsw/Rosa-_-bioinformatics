#! /usr/bin/python
import math

class xfinder:
    def __init__(self, L, c):
        self.dicPDP = []
        t = [x for x in L]
        t = sorted(t)
        self.maximumNumber = t[-1]
        del t[-1]
        self.tmp= [t[0]]
        for i in range(1,len(t)):
            if (t[i] != self.tmp[-1]):
                self.tmp.append(t[i])
        self.count = c
    def answer(self):
        vertex = [0]
        dicPDPs = 0
        for i in range(len(self.dicPDP)):
            dicPDPs += self.dicPDP[i]
            vertex.append(self.tmp[dicPDPs+i])
        vertex.append(self.maximumNumber)
        return vertex

    def combineNumber(self):
        if (len(self.dicPDP) == 0):
            # handles first t ime
            self.dicPDP = [0 for i in range(self.count)]
            return True
        else:
            #nextCombination(self.dicPDP, len(self.tmp))
            for i in range(len(self.dicPDP)-1,-1,-1):
                self.dicPDP[i] += 1
                if (sum(self.dicPDP) > len(self.tmp) - len(self.dicPDP)):
                    self.dicPDP[i] = 0
                else:
                    break
            
            return (sum(self.dicPDP) != 0)

if __name__ == "__main__":
    Lists = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 9, 9, 10, 11, 12, 15]
    counting = 0
    print(Lists)
    n = (math.sqrt(8 * len(Lists) + 1) + 1)/2
    if (int(n) != n):
        print("Invalid digest size")
    else:
        Lists = sorted(Lists)
        X = xfinder(Lists,int(n)-2)
        while (X.combineNumber()):
            _list = []
            val = X.answer() 
            for i in range(len(val)):
                for j in range(i+1, len(val)):
                    _list.append(val[j] - val[i])
            distributedX = _list
                    
            distributedX.sort()
            
            if(distributedX == Lists):
                counting += 1
                print("ANSWER", + counting, " = ", X.answer())

        