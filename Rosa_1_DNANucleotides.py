#import this
class solution:
    def main(self):
        print("counted number is ..")
        self.insert = "CATCTTCGACATTCCAGGTGATCACGTTAGTTAGTTGATTGCCGCTGCGATATAATTTAGGGGCGCTCGGACGTGGGAGGCCGGGAAAGGACGGACTGGGTATCCTGTTACTTTCTCCGGTGCTGACACGAGCGTAACCCTCTTGGCACTCGTCTCGCCCCAAGATCGCGGGTTTACCCCACAGTTCTACCTATTGACTGAAGTTAGCGGCACATATAGTGCAGTTAGTACCGTCGGATCTGCGATGACAACCCTCAGGTATCACACAAGTAACTTCCTCTAGCTTCAGCGTAGTCCGACGGGCATGCCGCGTTATTTCCCTTGATCCTGGGTATTATAGGGGGTACTTTTAGATACGTGGCATCTTGTGCTTTAATAAGAATGTCATTGAAAGTAGTCAGGGACTTATGGTTATAGTGGACGGTGCACGTAGGTGAATTAAACAATTGCGCCACCCAACTATATCTCCTTGGACCAGGACCACAAGCTTGACTCGTTGCTCCCGGCTAATGTTAGCGCCATGCGCCAAAGCTTACTGAGGGGACTGTTGTAAGCCATCGGGCATGGCGTGTACTGCGACGGAAGAGACCCCTACGTAAAGAACGGGATGCACACCCAAACTGAAACGACAACATGCTAGCCGGTCTGTCTCTACATTATTGAAGCCCAGATCAAATGGTTAACCCTTATAAATAAGTGTAATTTTTAGGTTTAGTGCCGTTTCGTACCTTTCTACAGGCCTCTGGTTGCTATCTGCAGCAAAGTACCATAGAAGCATATGTGACTCCTGAAAATATTCCAAGTCATACGTGGGCTTGCGACGTGGACATACCCTT"
        self.count = [0,0,0,0] # A C G T
        for i in self.insert:
            if i == "A":
                self.count[0] += 1
            elif i == "C":
                self.count[1] += 1

            elif i == "G":
                self.count[2] += 1

            elif i == "T":
                self.count[3] += 1
        print(self.count[0], self.count[1], self.count[2], self.count[3])
        #print(len(self.count))
        ans = [0] * 4
        ans[0] = self.count[0]
        ans[1] = self.count[1]
        ans[2] = self.count[2]
        ans[3] = self.count[3]
        print(ans)
        return ans

p = solution()
p.main()

"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            value = carry%10
            cur.next = ListNode(value)
            cur = cur.next
            carry //= 10 # 만약 10을 넘어가는 숫자가 있으면,, 그 숫자를 다음 계산할 때 1 더해줌. 
        return dummy.next
"""