"""
Manhattan algorithm(x, y, mat1, mat2)
v = 0
for i = 1 to x
    v(i, 0) = v(i-1, 0) + mat2(i, 0)
for i = 1 to x
    v(i, 0) = v(i-1, 0) + mat2(i, 0)
for i <- 1 to n
    for j <- 1 to m
    v(i,j) = max(v(i-1, j) + mat1(i,j), v(i,j-1) + mat2(i,j))
return v(x,y)
"""
def helper(x, y, mat1, mat2): 
    # Algorithm is above one
    v = {(0,0):0}
    for i in range(1,x+1):
        v[(i,0)] = v[(i-1,0)] + mat1[i-1][0]
    for i in range(1,y+1):
        v[(0,i)] = v[(0,i-1)] + mat2[0][i-1]
    for i in range(1,x+1):
        for j in range(1,y+1):
            v[(i,j)] = max(v[(i-1,j)] + mat1[i-1][j], v[(i,j-1)] + mat2[i][j-1])
    return v[(x,y)]
    
if __name__ == "__main__":
    # Main Function
    file = open('data.txt','r')
    first = file.readline().rstrip('\n')
    _intFirst = int(first[0])
    _intSecond = int(first[1])
    _intFirst = 10 * _intFirst
    f1 = _intFirst + _intSecond
    _intFirst2 = int(first[3])
    _intSecond2 = int(first[4])
    _intFirst2 = 10 * _intFirst2
    f2 = _intFirst2 + _intSecond2
    
    line_readers = file.readline().rstrip('\n')
    xyAxis =[]
    
    while line_readers != '-':
        xyAxis.append([int(i) for i in line_readers.split()])
        line_readers = file.readline().rstrip('\n') 

    lists = [[int(i) for i in line_readers.split()] for line_readers in file.readlines()]
    ret = helper(f1,f2,xyAxis,lists)
    
    print(ret)