
def mostProbableKmersInprofile(dna, k, profiles):
    ACGT = {t:index for index, t in enumerate('ACGT')}
    maxProbability = -1

    for i in range(len(dna)-k+1):
        curprob = 1
        for j, t in enumerate(dna[i:i+k]):
            curprob = curprob * profiles[j][ACGT[t]]

        if curprob > maxProbability:
            maxProbability = curprob
            mostprobabledna = dna[i:i+k]

    return mostprobabledna

"""
def mostProbableKmersInprofile2(dna, k, profile_maxtrix):
    letter = [[] for i in range(k)]
    hamdict = {}
    value = 1
    for i in range(k):
        for j in "ACGT":
            letter[i].append(profile_maxtrix[j][i])
    for i in slidingwindow(dna, k):
        for j in range(len(i)):
            if i[j] == "A":
                value *= float(letter[j][0])
            elif i[j] == "C":
                value *= float(letter[j][1])
            elif i[j] == "G":
                value *= float(letter[j][2])
            elif i[j] == "T":
                value *= float(letter[j][3])
        hamdict[i] = value
        value = 1
    for i, j in hamdict.items():
        if j == max(hamdict.values()):
            ans = i
            break
    return ans
"""
def slidingwindow(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i+k]

def score(motifs):
    columns = [''.join(i) for i in zip(*motifs)]
    maxCount = sum([max([c.count(i) for i in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - maxCount

def pseudocounts(motifs):
    prof = []
    for i in range(len(motifs[0])):
        col = ''.join([motifs[j][i] for j in range(len(motifs))])
        prof.append([float(col.count(j)+1)/float(len(col)+4) for j in 'ACGT'])
    return prof

def greedyMotifSearchAlgorithm(dna, k, t):
    scoreBest = k*t

    for i in range(len(dna[0])-k+1):
        motifs = [dna[0][i:i+k]]

        for j in range(1, t):
            curProf = pseudocounts(motifs)
            motifs.append(mostProbableKmersInprofile(dna[j], k, curProf))

        currentScore = score(motifs)
        if currentScore < scoreBest:
            scoreBest = currentScore
            bestMotifs = motifs

    return bestMotifs

if __name__ == '__main__':
    k = 12
    t = 25

    DNA2 = ['ADD Your DNA HERE']
    ans_kmers = greedyMotifSearchAlgorithm(DNA2, k, t)
    print('\n'.join(str(i) for i in ans_kmers))
