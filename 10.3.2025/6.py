from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    freq = Counter(s)
    freq =sorted(freq.items(),key=lambda x:x[1])
    print(s.replace(freq[0][0],freq[-1][0],1))