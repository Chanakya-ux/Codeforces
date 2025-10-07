def solve(l):
    c = [x for x in range(1, len(l) + 1)]
    k = [i for i in range(len(l)) if l[i] != c[i]]
    if k:
        return k[-1] - k[0] + 1
    else:
        return 0

for s in [*open(0)][2::2]:
    l = list(map(int, s.split()))
    if l.count(0) > 1 or l.count(0) == 0:
        print(solve(l))
    else:
        missingindex = [i for i, x in enumerate(l) if x == 0]
        missedvalue = (set(range(1,len(l)+1))-set(l)).pop()
        l[missingindex[0]] = missedvalue
        print(solve(l))
