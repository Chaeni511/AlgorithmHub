def attack(x, y):
    global res
    if board[x][y] == 'S':
        board[x][y] = 'F'
        res += 1
        for i in range(1, arr[x][y]):
            nx, ny = x + dx[D] * i, y + dy[D] * i
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 'S':
                attack(nx, ny)


N, M, R = map(int, input().split())  # col, row, round
arr = [list(map(int, input().split())) for _ in range(N)]
board = [['S']*M for _ in range(N)]
turn = [list(input().split()) for _ in range(R*2)]
res = 0

# E W S N
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for r in range(R*2):
    if r % 2 == 0:
        X, Y, D = turn[r]
        if D == 'E':
            D = 0
        elif D == 'W':
            D = 1
        elif D == 'S':
            D = 2
        else:
            D = 3
        attack(int(X)-1, int(Y)-1)
    else:
        X, Y = map(int, turn[r])
        board[X-1][Y-1] = 'S'

print(res)
for b in board:
    print(*b)