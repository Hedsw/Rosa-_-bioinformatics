def mainGreedy(DNAs, k, t):
    Output = []
    ScoreOfMotif = 100000000000
    for DNA in DNAs:
        Output.append(DNA[:k])
    for i in Slidingwindow(DNAs[0], k):
        _oneMotif = [i]
        for j in range(1, len(DNAs)):
            profile = BuildMatrix(_oneMotif)
            _oneMotif.append(ProfileMostProbable(DNAs[j], k, profile))
        if Findscore(_oneMotif) < ScoreOfMotif:
            ScoreOfMotif = Findscore(_oneMotif)
            Output = _oneMotif
    return Output

def HamDis(string1, string2):
    # Strings
    hamDis = 0
    for i in range(len(string1)):
        if len(string1) == len(string2):
            if string1[i] != string2[i]:
                hamDis += 1
    return hamDis

def Slidingwindow(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i+k]

def ProfileMostProbable(DNA, k, profile_maxtrix):
    letter = [[] for i in range(k)]
    hamdict = {}
    value = 1
    for i in range(k):
        for j in "ACGT":
            letter[i].append(profile_maxtrix[j][i])
    for i in Slidingwindow(DNA, k):
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

def Count(Motifs):
    count_set = {}
    k = len(Motifs[0])
    for i in "ACGT":
        count[i] = []
        for i in range(k):
            count_set[i].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            _char = Motifs[i][j]
            count_set[_char][j] += 1
    return count_set

def BuildMatrix(motifs):
    ProfileMatrix = {}
    A, C, G, T = [], [], [], []
    for j in range(len(motifs[0])):
        counts = [0,0,0,0]
        for motif in motifs:
            if motif[j] == "A":
                counts[0] += 1
            elif motif[j] == "C":
                counts[1] += 1
            elif motif[j] == "G":
                counts[2] += 1
            elif motif[j] == "T":
                counts[3] += 1
        A.append(counts[0])
        C.append(counts[1])
        G.append(counts[2])
        T.append(counts[3])
    ProfileMatrix["A"] = A
    ProfileMatrix["C"] = C
    ProfileMatrix["G"] = G
    ProfileMatrix["T"] = T
    return ProfileMatrix

def Findscore(motifs):
    _consensus = ""
    ret = 0
    for i in range(len(motifs[0])):
        counts = [0,0,0,0] # A C G T
        for motif in motifs:
            if motif[i] == "A":
                counts[0] += 1
            elif motif[i] == "C":
                counts[1] += 1
            elif motif[i] == "G":
                counts[2] += 1
            elif motif[i] == "T":
                counts[3] += 1
        if counts[0] >= counts[1] and counts[0] >= counts[2] and counts[0] >= counts[3]:
            _consensus += "A"
        elif counts[1] >= counts[0] and counts[1] >= counts[2] and counts[1] >= counts[3]:
            _consensus += "C"
        elif counts[2] >= counts[0] and counts[2] >= counts[1] and counts[2] >= counts[3]:
            _consensus += "G"
        elif counts[3] >= counts[1] and counts[3] >= counts[2] and counts[3] >= counts[0]:
            _consensus += "T"

    for motif in motifs:
        ret += HamDis(_consensus, motif)
    return ret

if __name__ == "__main__":
    DNAs = ['ADD',
            'Your', 
            'DNA',
            'HERE'
            ]
    k = 12
    t = 25
    ans = mainGreedy(DNAs, k, t)
    print(' '.join(ans))