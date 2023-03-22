import copy
def clean(x, y):
    global res, d
    if not visited[x][y]:
        res += 1
        visited[x][y] = 1
    # else:
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        if 0 <= nx < N and 0 <= ny < M and not room[nx][ny] and not visited[nx][ny]:
            # 3-1. 반시계 방향으로 90도 회전한다.
            d = dir_r[(dir_r.index(d) + 1) % 4]
            t = dir_b.index(d)
            tx, ty = x + dx[t], y + dy[t]
            # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            if 0 <= tx < N and 0 <= ty < M and not room[tx][ty] and not visited[tx][ty]:
                clean(tx, ty)
                return
            else:
                clean(x, y)
                return
            # break
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    else:
        # 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        b = dir_b.index((d+2) % 4)
        nx, ny = x + dx[b], y + dy[b]
        if 0 <= nx < N and 0 <= ny < M and not room[nx][ny]:
            clean(nx, ny)
            return
        # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            return

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)] # 빈칸 여부
visited = copy.deepcopy(room) # 청소 여부

# 동 북 서 남 (반시계)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
# 북 동 남 서
dir_b = [1, 0, 3, 2]
dir_r = [0, 3, 2, 1]

res = 0
clean(r, c)
print(res)
