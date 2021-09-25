def mostprobable(_str, k, matrix):
    k_str = ""
    max_str = ""
    max_num = 0
    for i in range(len(_str)+1 - k): # length of matrix row
        k_str = _str[i:k+i]
        mult_num = 1
        tmp = 0
        for j in range(k):
            if k_str[j] == 'A':
                tmp = matrix[0][j]
                #print(tmp, matrix[0][i])
                #print(k_str[j], k_str, tmp)
            elif k_str[j] == 'C':
                tmp = matrix[1][j]
                #print(k_str[j], k_str, tmp)
            elif k_str[j] == 'G':
                tmp = matrix[2][j]
                #print(k_str[j], k_str, tmp)
            elif k_str[j] == 'T':
                tmp = matrix[3][j]                
                #print(k_str[j], k_str, tmp)
            mult_num = mult_num * tmp
        if max_num < mult_num:
            max_num = mult_num
            max_str = k_str
        mult_num = 0
        #print(max_num)
        print(max_str)

if __name__ == "__main__":

    _str = "CCGCTTAATGATTGCCCTATAGACCTAGAATATGGAAACGCACGAGCGATGAAGACCGTCCGATACTAACGCGAAAGTAGTTTCGCCATGACGGGTAGCATTGACGCGGCTGTCCCTCAGACGTTATATATATAGGAGCATCTAATCAAAATCGCTAGAGACCGTTTTGTAAACTCCACCGCGACAGTCGAGGTCAATGT"
    k = 6
    matrix = [
        [0.091,0.242,0.303,0.182,0.303,0.333],
        [0.303,0.303,0.152,0.333,0.152,0.182],
        [0.182,0.182,0.242,0.182,0.242,0.152],
        [0.424,0.273,0.303,0.303,0.303,0.333]
        ]
    ans = mostprobable(_str, k, matrix)
