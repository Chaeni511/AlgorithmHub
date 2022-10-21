from collections import deque

N, M = map(int, input().split())
target = list(map(int, input().split()))
Q = deque()
for _ in range(1, N+1):
    Q.append(_)
cnt = 0

for t in target:
    q = Q.index(t)
    if q == 0:
        pass
    elif q <= len(Q)//2:
        Q.rotate(-q)
        cnt += q

    elif q > len(Q)//2:
        Q.rotate(len(Q) - q)
        cnt += len(Q) - q
    Q.popleft()

print(cnt)