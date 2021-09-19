from itertools import product, combinations
from collections import defaultdict

class solution:
    def main(self, string1, kfreq, mismatch_num, _listSubs, _allNumCom):
        # Strings
        self._dict = defaultdict(int)

        for i in range(len(string1)):
            _char = string1[i:i+kfreq]
            if len(_char) < kfreq:
                break
            if _char in self._dict:
                self._dict[_char] += 1
            else:
                self._dict[_char] = 1
            
            dupcheck = set([_char])
            _newlist = list(_char)                
            for iCom in _allNumCom:
                _tmp = [_newlist[i] for i in iCom]
                for news in _listSubs:
                    for i, new in zip(iCom, news):
                        _newlist[i] = new
                    ans = " ".join(_newlist)
                    if ans not in dupcheck:
                        dupcheck.add(ans)
                        self._dict[ans] += 1
                
                for i, j in zip(iCom, _tmp):
                    _newlist[i] = j
        
        maxFreq = max(self._dict.values())

        for key in self._dict:
            if self._dict[key] == maxFreq:
                print(key)


if __name__ == "__main__":
    p = solution()
    string1 = "STRING HERE"
    kfreq = 7
    mismatch_num = 3
    _listSubs = list(product("ACGT", repeat = mismatch_num))
    _allNumCom = list(combinations(range(kfreq), mismatch_num))

    p.main(string1, kfreq, mismatch_num, _listSubs, _allNumCom)

