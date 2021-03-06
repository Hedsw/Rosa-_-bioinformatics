class solution:
    def main(self, k, l, t, string):
        # Strings
        self.insert = string
        self.ans = 0
        
        # A string Genome and integers k (length of a pattern), L
        # (window length), and t (number of patterns in a clump). 
        _dict = {}
        
        for j in range(len(string)-k + 1):
            self.insert_new = string[j:l+j]
            kmer = string[j: j + k]
            
            if kmer in _dict:
                _dict[kmer] += 1
            else:
                _dict[kmer] = 1

        #print(_dict)
        _dictfreq = {}
        
        for i in _dict:
            if _dict[i] >= t:
                _dictfreq[i] = _dict[i]
            
        ans = _dictfreq.keys()
        print(ans)
        

if __name__ == "__main__":
    #print("World?")
    p = solution()
    k = 12
    l = 513
    t = 17
    string = "String"
    p.main(k, l, t, string)
