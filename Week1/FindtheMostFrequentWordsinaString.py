class solution:
    def main(self):
        # Strings
        self.insert = "StringHere" 
        # Target Count
        self.target = "GTACTTAGT" 
        lenTarget = len(self.target)
        lenInsert = len(self.insert)
        ans = 0
        count = 0
        print(self.insert[count+0:lenTarget+0])
        for i in range(len(self.insert)):
            if self.target == self.insert[count+i:lenTarget+i]:
                ans = ans + 1
        print(ans)
        return ans

p = solution()
p.main()
