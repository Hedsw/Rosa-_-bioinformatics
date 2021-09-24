
class mismatches:
    def mismatch(self, _setDNA, test, d):
        _mismatches = 0
        for i in range(len(_setDNA)):
            if _mismatches <= d:
                if _setDNA[i] != test[i]:
                    _mismatches += 1
            else:
                break
        if _mismatches <= d:
            return True
        else:
            return False

class Motifs:
    def motif(self, DNA, k, d):
        shared = False
        shares = 0
        
        for i in DNA:
            found = False
            for j in range(len(i), len(k)):
                test = i[j:j+len(k)]
                if mismatches.mismatch(k, test, d) <= d:
                    print(k + " " + test)
                    found = True
                    shares += 1
                    break
            if found == False:
                break
            
        if shares == len(DNA):
            shared = True
        return shared
               

class MotifEnumeration:
    def motifenumberation(self, DNA, k, d):
        _setDNA = set()
        
        for i in DNA:        
            for j in range(len(DNA[i])):
                if j+3 <= len(DNA[i]):
                    pattern = _setDNA[i:i+k]
                    for m in range(len(_setDNA) - k):
                        test = i[m:m+k]
                        if mismatches.mismatch(pattern, test, d) and Motifs.motif(DNA, test, d):
                            _setDNA.add(test)
                            
                            
        # Strings
        print(k , d)
        #print(DNA)
     
        
        
if __name__ == "__main__":
    p = MotifEnumeration()
    DNA = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
    k = 3
    d = 1
    p.motifenumberation(DNA, k, d)
