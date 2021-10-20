from collections import Counter
result = []
intercheck = 0    
def turnpikehelper(_list, r, w):
    if _list == []:
        result.append(sorted(r))
        #intercheck += 1
        return
    maxL = max(_list)
    absY = [abs(maxL - i) for i in r]
    absw = [abs(w - maxL - i) for i in r]

    if Counter(absY) == (Counter(absY) & Counter(_list)):
        r.append(maxL)
        for i in absY:
            _list.remove(i)
        turnpikehelper(_list, r, w)
        r.remove(maxL)
        for i in absY:
            _list.append(i)

    if Counter(absw) == (Counter(absw) & Counter(_list)):
        r.append(w - maxL)
        for i in absw:
            _list.remove(i)
        turnpikehelper(_list, r, w)
        r.remove(w - maxL)
        for i in absw:
            _list.append(i)
    
if __name__== '__main__':
    _list = [int(i) for i in open('data.txt').readline().split()]
    newL = []
    for i in range(len(_list)):
        if _list[i] > 0:
            newL.append(_list[i])
    maxnum = max(newL)
    newL.remove(maxnum)
    Lrange = [0, maxnum]
    turnpikehelper(newL, Lrange, maxnum)
    
    ans = ""
    for i in result[0]:
        #print(str(i))
        ans += str(i)
        ans += " "
        
    print(ans)
    #print("Iter..", intercheck)