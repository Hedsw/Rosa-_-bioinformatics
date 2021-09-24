class solution:
    def main(self,string1, string2):
        # Strings
        hamDis = 0
        for i in range(len(string1)):
            if len(string1) == len(string2):
                if string1[i] != string2[i]:
                    hamDis += 1
        print(hamDis)    
        

if __name__ == "__main__":
    p = solution()
    string1 = "String1"
    string2 = "String2"
    p.main(string1, string2)
