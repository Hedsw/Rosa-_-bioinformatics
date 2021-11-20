# Reference: https://vlab.amrita.edu/?sub=3&brch=274&sim=1433&cnt=1

from numpy import *
def longestcorrespondSequence(v, w):
    matrix_score = zeros((len(v)+1,len(w)+1), dtype="float64")
    matrix_backtracking = zeros((len(v)+1,len(w)+1), dtype="float64")
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            # find best score at each vertex
            # This case is matched
            if (v[i-1] == w[j-1]):    
                matrix_score[i,j], matrix_backtracking[i,j] = max((matrix_score[i-1,j-1] + 1, 3), # Match is + 1
                                             (matrix_score[i-1,j] - 0.5, 1), # Indel is -0.5
                                             (matrix_score[i,j-1] - 0.5, 2)) # Indel is -0.5
            # v[i-1] == w[j-i] -> Unmatch or Indel (right arrow and down arrow)
            else:
                matrix_score[i,j], matrix_backtracking[i,j] = max((matrix_score[i-1,j-1] -1, 3), # Mis Match is -1
                                             (matrix_score[i-1,j] -0.5 ,1), # Indel is -0.5
                                             (matrix_score[i,j-1] -0.5 ,2)) # Indel is -0.5
    return (matrix_score, matrix_backtracking)
matrix, backtracking = longestcorrespondSequence("1213434222","1343422421")
print ("score matrix =\n", matrix)

def OptimalAlign(backtracking,v,w,i,j):
    if ((i == 0) and (j == 0)):
        return ['','']
    if (backtracking[i,j] == 3): # Which is bi-directional path
        ret = OptimalAlign(backtracking,v,w,i-1,j-1)
        ret[0] += v[i-1]
        ret[1] += w[j-1]
        return ret
    else:
        if (backtracking[i,j] == 2): # Which is down path (Indel)
            ret = OptimalAlign(backtracking,v,w,i,j-1)
            ret[0] += "-" # Indel so that we have to "-" to the string
            ret[1] += w[j-1]
            return ret
        else:
            ret = OptimalAlign(backtracking,v,w,i-1,j) # Which is right path (Indel)
            ret[0] += v[i-1]  # Indel so that we have to "-" to the string
            ret[1] += "-"
            return ret
        
ans = OptimalAlign(backtracking,"1213434222","1343422421",backtracking.shape[0]-1,backtracking.shape[1]-1)
print("v =", ans[0])
print("w =", ans[1])


