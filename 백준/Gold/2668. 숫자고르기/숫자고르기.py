import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]


def dfs(r1):
    row1[r1-1] = 1

    r2 = arr[r1-1]
    if not row2[r2-1]:
        row2[r2-1] = 1
        dfs(r2)


ans = 0
ans_arr = [0] * N

for i in range(1, N+1):
    row1 = [0] * N
    row2 = [0] * N

    dfs(i)
    if row2 == row1:
        for n in range(N):
            if row1[n]:
                ans_arr[n] = 1

for n in range(N):
    if ans_arr[n]:
        ans += 1
print(ans)

for n in range(N):
    if ans_arr[n]:
        print(n+1)

