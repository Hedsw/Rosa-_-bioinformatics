from collections import Counter
class solution:
    def main(self):     
        counts = set()
        listCount = []
        # Strings
        self.insert = "ACGTTGCATGTCGCATGATGCATGAGAGCT" 
        # Target Count
        self.strLeng = 4
        
        for i in range(len(self.insert)):
            if i+self.strLeng <= len(self.insert):
                listCount.append(self.insert[i:i+self.strLeng])
        
        #print(listCount)
        print(Counter(listCount))
        #return counts
        
        
p = solution()
p.main()




