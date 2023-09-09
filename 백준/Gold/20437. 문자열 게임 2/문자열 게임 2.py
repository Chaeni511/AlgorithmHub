import sys
from collections import defaultdict

T = int(sys.stdin.readline())

for t in range(T):
    W = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())

    dict = defaultdict(list)

    for i, w in enumerate(W):
        if W.count(w) >= K:
            dict[w].append(i)

    a = 987654321
    b = 0

    for key in dict.keys():
        for i in range(len(dict[key]) - K + 1):
            if dict[key][i+K-1] - dict[key][i] + 1 < a:
                a = dict[key][i+K-1] - dict[key][i] + 1
            if dict[key][i+K-1] - dict[key][i] + 1 > b:
                b = dict[key][i+K-1] - dict[key][i] + 1
                
    if not b:
        print(-1)
    else:
        print(a, b)
