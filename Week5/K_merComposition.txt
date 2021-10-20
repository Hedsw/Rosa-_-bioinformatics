def debrujin(strings):
    kmers = []
    dicts = {}
    for str in strings:
        tmp = []
        for i in range(1):
            tmp.append(str[i:i+len(str)-1])
        kmers += sorted(list(tmp))
    kmersset = set(kmers)
    for kmer in kmersset:
        dicts[kmer] = []
    for str in strings:
        dicts[str[:-1]].append(str[1:])
    return dicts

def euleriancheck(dupcheck):
    lists=[]
    path = []
    counts = dupcheck.fromkeys(dupcheck.keys(), 0)
    for key in dupcheck.keys():
        for i in dupcheck[key]:
            counts[key] -= 1
            try:
                counts[i] += 1
            except:
                counts[i] = 1
    lists.append([i for i, vertex in counts.items() if vertex==-1][0])
    while lists != []:
        pos = lists[-1]
        try:
            tmp = dupcheck[pos][0]
            lists.append(tmp)
            dupcheck[pos].remove(tmp)
        except:
            path.append(lists.pop())
    return path[::-1]

if __name__ == "__main__":
    lists = [] 
    file = open('text.txt', 'r')
    lines = file.readlines()
    
    for i in range(1, len(lines)-1):
        lists.append(lines[i][:-1])
    lists.append(lines[-1])
    print(lists)
    getbrugin = debrujin(lists)
    eulerian = euleriancheck(getbrugin)
    
    ans = ''
    for kmer in eulerian:
        ans += kmer[0]
    ans += kmer[1:]    
    print(ans)