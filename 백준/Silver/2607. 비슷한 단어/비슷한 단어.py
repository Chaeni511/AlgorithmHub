import copy

N = int(input())
res = 0

target = list(input())

for _ in range(N-1):
    w1 = copy.deepcopy(target)
    w2 = input()
    cnt = 0
    for i in w2:
        if i in w1:
            w1.remove(i)
        else:
            cnt += 1
    if cnt < 2 and len(w1) < 2:
        res += 1
print(res)
