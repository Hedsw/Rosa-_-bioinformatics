class MotifEnumeration:
    def main(self, DNA, k, d):
        _setDNA = {}
        
        _setDNA.add(DNA[0])
        # Strings
        print(k , d)
        print(DNA)
        
        

if __name__ == "__main__":
    p = MotifEnumeration()
    DNA = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
    k = 3
    d = 1
    p.main(DNA, k, d)
