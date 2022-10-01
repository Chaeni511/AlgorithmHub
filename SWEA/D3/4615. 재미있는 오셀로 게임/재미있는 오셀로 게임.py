'''
1 흑돌
2 백돌
21
12
'''


def othello(sx, sy, c):
    for i in range(8):
        flag = False
        nx = sx + dx[i]
        ny = sy + dy[i]
        while 0 < nx <= N and 0 < ny <= N:
            if board[nx][ny] == 0:
                break
            if board[nx][ny] == c:
                flag = True
                ex, ey = nx, ny
                break
            nx += dx[i]
            ny += dy[i]
        if flag:
            nx, ny = sx, sy
            while not (nx == ex and ny == ey):
                nx += dx[i]
                ny += dy[i]
                board[nx][ny] = c


dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*(N+1) for _ in range(N+1)]

    # 초기 설정
    n = N//2
    board[n][n+1] = board[n+1][n] = 1
    board[n][n] = board[n+1][n+1] = 2

    for i in range(M):
        x, y, c = map(int, input().split())
        board[x][y] = c
        othello(x, y, c)

    B = W = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 1:
                B += 1
            elif board[i][j] == 2:
                W += 1
    print(f'#{tc} {B} {W}')
