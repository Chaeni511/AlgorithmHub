from collections import deque


def f():
    global cnt
    while Q:
        imp, idx = Q.popleft()
        for i in range(len(Q)):
            if Q[i][0] > imp:
                Q.append((imp, idx))
                break
        else:
            cnt += 1
            if idx == M:
                return cnt


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = deque()
    for i in range(N):
        Q.append((arr[i], i))
    cnt = 0
    print(f())