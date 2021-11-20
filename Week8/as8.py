from numpy import *

def longestcorrespondSequence(v, w):
    score = zeros((len(v)+1,len(w)+1), dtype="float64")
    backt = zeros((len(v)+1,len(w)+1), dtype="float64")
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            # find best score at each vertex
            # This case is matched
            if (v[i-1] == w[j-1]):    
                score[i,j], backt[i,j] = max((score[i-1,j-1] + 1, 3), # Match is + 1
                                             (score[i-1,j] - 0.5, 1), # Indel is -0.5
                                             (score[i,j-1] - 0.5, 2)) # Indel is -0.5
            # v[i-1] == w[j-i] -> Unmatch or Indel 
            else:
                score[i,j], backt[i,j] = max((score[i-1,j-1] -1, 3), # Mis Match is -1
                                             (score[i-1,j] -0.5 ,1), # Indel is -0.5
                                             (score[i,j-1] -0.5 ,2)) # Indel is -0.5
    return (score, backt)
score, backtracking = longestcorrespondSequence("1213434222","1343422421")
print ("score =\n", score)
#print ("\nbacktrack =\n", b)

def OptimalAlign(backtracking,v,w,i,j):
    if ((i == 0) and (j == 0)):
        return ['','']
    if (backtracking[i,j] == 3): # Which is backtrackingidirectional path
        ret = OptimalAlign(backtracking,v,w,i-1,j-1)
        ret[0] += v[i-1]
        ret[1] += w[j-1]
        return ret
    else:
        if (backtracking[i,j] == 2): # Which is down path (Indel)
            ret = OptimalAlign(backtracking,v,w,i,j-1)
            ret[0] += "-"
            ret[1] += w[j-1]
            return ret
        else:
            ret = OptimalAlign(backtracking,v,w,i-1,j) # Which is right path (Indel)
            ret[0] += v[i-1]
            ret[1] += "-"
            return ret
        
ans = OptimalAlign(backtracking,"1213434222","1343422421",backtracking.shape[0]-1,backtracking.shape[1]-1)
print("v =", ans[0])
print("w =", ans[1])


