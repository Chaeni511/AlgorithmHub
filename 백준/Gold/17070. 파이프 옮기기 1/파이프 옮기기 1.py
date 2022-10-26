
N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
cnt = 0


def dfs(x, y, d):   # 파이프 끝의 x좌표, y좌표, 현재 파이프가 놓인 방향
    global cnt
    if (x, y) == (N-1, N-1):
        cnt += 1
        return

    # 현재 파이프 방향: 가로
    if d == 0:
        if y+1 < N and house[x][y+1] == 0:
            dfs(x, y+1, 0)
        if y+1 < N and x+1 < N and house[x][y+1] == 0 and house[x+1][y] == 0 and house[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)

    # 현재 파이프 방향: 세로
    elif d == 1:
        if x+1 < N and house[x+1][y] == 0:
            dfs(x+1, y, 1)
        if y+1 < N and x+1 < N and house[x][y+1] == 0 and house[x+1][y] == 0 and house[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)

    # 현재 파이프 방향: 대각선
    else:
        if y+1 < N and house[x][y+1] == 0:
            dfs(x, y+1, 0)
        if x+1 < N and house[x+1][y] == 0:
            dfs(x+1, y, 1)
        if y+1 < N and x+1 < N and house[x][y+1] == 0 and house[x+1][y] == 0 and house[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)


# 파이프 방향
# 0 가로
# 1 세로
# 2 대각

dfs(0, 1, 0)
print(cnt)
