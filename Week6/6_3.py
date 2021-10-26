X = []
width = 0
import timeit

def removelengthYX(y, X, L):
    for xs in X:
        if abs(y - xs) in L:
            L.remove(abs(y - xs))
def chcker(value, _setX, total):
    for xs in _setX:
        if abs(value-xs) not in total:
            return False
    return True

def mainPD(L):
    global X, width
    width = max(L)
    L.remove(width)
    X = [0, width]
    recursivePlace(L, X)  

def recursivePlace(L, X):
    if not L:
        print("X: ", X)
        return
    maxVal = max(L)

    if chcker(maxVal, X, L):
        X.append(maxVal)
        removelengthYX(maxVal, X, L)
        recursivePlace(L, X)
        if maxVal in X:
            X.remove(maxVal)        
        lists = []
        for xs in X:
            lists.append(abs(maxVal-xs))
        L.extend(lists)

    if chcker(abs(width-maxVal), X, L):
        X.append(abs(width-maxVal))
        removelengthYX(abs(width-maxVal), X, L)
        recursivePlace(L, X)
        if abs(width-maxVal) in X:
            X.remove(abs(width-maxVal))
        lists = []
        for xs in X:
            tmp = abs(width-maxVal)
            lists.append(abs(tmp-xs))
        L.extend(lists)

if __name__ == "__main__":
    start = timeit.default_timer()
    L = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 9, 9, 10, 11, 12, 15]
    print("Partial Digest Result: ")
    mainPD(L)
    stop = timeit.default_timer()
    print('Time: ', stop - start)  