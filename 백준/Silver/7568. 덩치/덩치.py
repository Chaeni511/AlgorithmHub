import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rank = [0] * N      # 자신보다 덩치가 큰 사람의 수
for i in range(N):
    x, y = arr[i][0], arr[i][1]
    for j in range(N):
        p, q = arr[j][0], arr[j][1]
        if x < p and y < q:
            rank[i] += 1

# 등수로 변환
r = [e for e in range(1, N+1)]
for i in range(N):
    rank[i] = r[rank[i]]

print(' '.join(map(str, rank)))
