import itertools
def combination(k):
    return (''.join(p) for p in itertools.product('ATCG', repeat=k))

def hum_dis(pattern, seq):
    distance = 0
    for i in range(len(pattern)):
        if len(pattern) == len(seq) and pattern[i] != seq[i]:
            distance +=1
    return distance

def kmerchecker(m, k):
    for i in range(len(m) - (k-1)):
        yield m[i:i+k]
        
def kmerchecker_in(combo, DNA, k, d):
    checker = False
    for i in kmerchecker(DNA, k):
        if hum_dis(combo, i) <= d:
            checker = True
    return checker      

def motif_enumeration(k, d, DNAs):
    pattern = set()
    for combo in combination(k):
        if all(kmerchecker_in(combo, DNA, k, d) for DNA in DNAs):
            pattern.add(combo)
            
    return pattern

if __name__ == "__main__":

    DNAs = ['TTGCCAAGGTCCTGTCTGGCGGCAA', 'ACTGATCGAGCCGTACAGGTCGCTA', 'TTAGGACTGACAGGATTACAACGTG', 'CATAGGTATCTGTAGTCTACAAGGG','CTCCCTTATACGCTTCTGCAGAGGG', 'ACAGAGCGTGACCAGCTATCGAGGG','GGATCGGCATGAGGTCGGGTAAAAG', 'CAGGACTTGCTCCTTTGTGGTTCAC', 'CAGGGGGGATCTGCTGGGTGATTCG', 'GCTCGAGGAAGAGGATGTTAGAAGA']
    ans = motif_enumeration(5, 2, DNAs)

    #print(list(ans))
    print(' '.join(ans))