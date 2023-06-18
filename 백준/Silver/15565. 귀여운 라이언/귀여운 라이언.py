N, K = map(int, input().split())
dolls = list(map(int, input().split()))

res = int(1e9)
ryan = 0
s = e = 0

if dolls[e] == 1:
    ryan += 1
    
while e < N:
    if ryan >= K:
        res = min(e - s + 1, res)
        if dolls[s] == 1:
            ryan -= 1
        s += 1
    else:
        e += 1
        if e < N and dolls[e] == 1:
            ryan += 1

if res == int(1e9):
    res = -1
    
print(res)
