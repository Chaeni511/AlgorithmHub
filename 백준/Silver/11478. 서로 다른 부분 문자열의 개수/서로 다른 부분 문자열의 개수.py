import sys
S = sys.stdin.readline()
arr = []
for i in range(len(S)):
    for j in range(len(S) - 1 - i):
        arr.append(S[j:j+1+i])

print(len(set(arr)))