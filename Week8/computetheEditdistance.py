def minDistance(word1, word2):
    #DP solution
    m = len(word1)
    n = len(word2)
    tb = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        tb[i][0] = i
    for j in range(n + 1):
        tb[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                tb[i][j] = tb[i - 1][j - 1]
            else:
                # This condition is indel and unmatched cases 
                # So that we could choose minimum values in the three cases
                tb[i][j] = 1 + min(tb[i - 1][j], tb[i][j - 1], tb[i - 1][j - 1])
    return tb[-1][-1]
        
given = "TEXT1"
_str = "TEXT2"

print(minDistance(given, _str))

