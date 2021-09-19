from itertools import product, combinations
from collections import defaultdict

def fwm(g, k, d): # d = mismatch_num, k = kfreq, g = string1
	all_subs = list(product("ACGT", repeat=d))
	print(all_subs[0])
	all_ixs = list(combinations(range(k), d))
	patcount = defaultdict(int)

	#print(all_subs)
	for starti in range(len(g)):
		base = g[starti : starti + k]
		if len(base) < k:
			break
		patcount[base] += 1
		seen = set([base])
		basea = list(base)
		for ixs in all_ixs:
			saved = [basea[i] for i in ixs]
			for newchars in all_subs:
				for i, newchar in zip(ixs, newchars):
					basea[i] = newchar
				candidate = "".join(basea)
				if candidate not in seen:
					seen.add(candidate)
					patcount[candidate] += 1
			for i, ch in zip(ixs, saved):
				basea[i] = ch
				
    maxcount = max(patcount.values())
    return [p for p, c in patcount.items() if c == maxcount]

if __name__ == "__main__":
    #print("World?")
    #p = fwm()
    string1 = "CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC"
    kfreq = 10
    mismatch_num = 2
    print(fwm(string1, kfreq, mismatch_num))
