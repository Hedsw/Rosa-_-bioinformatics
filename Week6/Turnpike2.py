from collections import Counter
result = []
def turnpikehelper(_list, Lrange, maxnum):
    if _list == []:
        result.append(sorted(Lrange))
        return
    maxL = max(_list)
    absY = [abs(maxL - i) for i in Lrange]
    absw = [abs(maxnum - maxL - i) for i in Lrange]

    if Counter(absY) == (Counter(absY) & Counter(_list)):
        # if absY is same with Counter(absY) AND _list Counter
        Lrange.append(maxL)
        for i in absY:
            _list.remove(i)
        turnpikehelper(_list, Lrange, maxnum)
        Lrange.remove(maxL)
        for i in absY:
            _list.append(i)

    if Counter(absw) == (Counter(absw) & Counter(_list)):
        # Do twice  
        # if absY is same with Counter(absY) AND _list Counter
        Lrange.append(maxnum - maxL)
        for i in absw:
            _list.remove(i)
        turnpikehelper(_list, Lrange, maxnum)
        Lrange.remove(maxnum - maxL)
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
        ans += str(i)
        ans += " "
        
    print(ans)
