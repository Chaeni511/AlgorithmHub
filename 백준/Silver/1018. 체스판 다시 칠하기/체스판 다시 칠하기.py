N, M = map(int, input().split())    # 세로, 가로
board = [list(input()) for _ in range(N)]
res = 987654321

for i in range(N-7):
    for j in range(M-7):
        w = b = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if x % 2 == y % 2:
                    if board[x][y] == 'W':
                        w += 1
                    else:
                        b += 1
                elif x % 2 != y % 2:
                    if board[x][y] == 'B':
                        w += 1
                    else:
                        b += 1
        res = min(res, w, b)

print(res)