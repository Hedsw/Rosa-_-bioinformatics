from collections import Counter

class solution:
    def main(self):
        # Strings
        self.insert = " Type your string here" 
        insertlist = list(self.insert)
        insertlist.reverse()
        answer = ""
        for i in insertlist:
            if i == "A":
                answer = answer + "T"
            elif i == "T":
                answer = answer + "A"
            elif i == "C":
                answer = answer + "G"
            elif i == "G":
                answer = answer + "C"
        print(answer)
        return answer
p = solution()
p.main()
