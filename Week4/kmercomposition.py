

if __name__ == "__main__":

    _str = "ADD DNA HERE"
    k = 50
    ans = []
    for i in range(len(_str)):
        if k + i <= len(_str):
            ans.append(_str[i:k+i])
    
    print('\n'.join(str(i) for i in sorted(ans)))
