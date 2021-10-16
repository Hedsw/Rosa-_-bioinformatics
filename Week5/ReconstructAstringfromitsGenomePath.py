
def getgenomepath(lists):
    #print("TEST")
    ans = lists[0] 
    
    for i in range(1, len(lists)):
        ans += lists[i][-1]
    ans += lists[-1][-1]
    print(ans[0:-1])

if __name__ == "__main__":
    lists = [] 
    file1 = open('data.txt', 'r')
    lines = file1.readlines()
    
    for i in range(0, len(lines)-1):
        lists.append(lines[i][0:-1])
    lists.append(lines[-1])
    print(lists)
             
    getgenomepath(lists)
    