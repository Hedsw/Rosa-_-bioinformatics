def helper(x, y, matrix2, matrix1): 
    _xAxisyAxis = {(0,0):0}
    
    for i in range(1,x+1):
        _xAxisyAxis[(i,0)] = _xAxisyAxis[(i-1,0)] + matrix2[i-1][0]
        
    for j in range(1,y+1):
        _xAxisyAxis[(0,j)] = _xAxisyAxis[(0,j-1)] + matrix1[0][j-1]

    for i in range(1,x+1):
        for j in range(1,y+1):
            _xAxisyAxis[(i,j)] = max(_xAxisyAxis[(i-1,j)]+matrix2[i-1][j], _xAxisyAxis[(i,j-1)] + matrix1[i][j-1])

    return _xAxisyAxis[(x,y)]
    

if __name__ == "__main__":
    file = open('data.txt','r')
    _nValue = int(file.readline().rstrip('\n') )
    _mValue = int(file.readline().rstrip('\n') )
    f_reader = file.readline().rstrip('\n')
    matrix2 =[]
    while f_reader != '-':
        matrix2.append([int(i) for i in f_reader.split()])
        f_reader = file.readline().rstrip('\n') 

    matrix1 = [[int(i) for i in f_reader.split()] for f_reader in file.readlines()]
    output = helper(_nValue,_mValue,matrix2,matrix1)
    
    with  open('output.txt','w') as fout:
        fout.write ("%s\n" % str(output) )
