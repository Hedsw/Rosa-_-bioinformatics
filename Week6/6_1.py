def mulset(xs):
    multiset = []
    for x in range(len(xs)):
        for j in range(x+1, len(xs)):
            #print(xs[j] - xs[x])   
            multiset.append(xs[j] - xs[x])         
    print(multiset)
if __name__ == "__main__":
    x = [0, 3, 8, 10]
    mulset(x)
    