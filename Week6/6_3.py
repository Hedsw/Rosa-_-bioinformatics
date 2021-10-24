X = []
L = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 9, 9, 10, 11, 12, 15]
width = 0
import timeit

def removelengthYX(y, X, L):
    for xs in X:
        if abs(y - xs) in L:
            L.remove(abs(y - xs))
def isexist(y, X, L):
        for xs in X:
            if abs(y-xs) not in L:
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
    y = max(L)

    if isexist(y, X, L):
        X.append(y)
        removelengthYX(y, X, L)
        recursivePlace(L, X)
        if y in X:
            X.remove(y)        
        lists = []
        for xs in X:
            lists.append(abs(y-xs))
        L.extend(lists)

    if isexist(abs(width-y), X, L):
        X.append(abs(width-y))
        removelengthYX(abs(width-y), X, L)
        recursivePlace(L, X)
        if abs(width-y) in X:
            X.remove(abs(width-y))
        lists = []
        for xs in X:
            tmp = abs(width-y)
            lists.append(abs(tmp-xs))
        L.extend(lists)

if __name__ == "__main__":
    start = timeit.default_timer()

    print("Partial Digest Result: ")
    mainPD(L)
    stop = timeit.default_timer()
    print('Time: ', stop - start)  