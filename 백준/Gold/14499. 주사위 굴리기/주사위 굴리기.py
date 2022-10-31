N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
dice = [0]*6

# dice index    East     West     North     South       dice
#     3          3        3         0         5          d
#   2 0 1      0 1 5    5 2 0     2 4 1     2 3 1      c a b
#     4          4        4         5         0          e
#     5          2        1         3         4          f


def roll(d):
    global dice
    global x, y
    if d == 1:
        if 0 <= y+1 < M:
            dice = [dice[1], dice[5], dice[0], dice[3], dice[4], dice[2]]
            y += 1
        else:
            return
    elif d == 2:
        if 0 <= y - 1 < M:
            dice = [dice[2], dice[0], dice[5], dice[3], dice[4], dice[1]]
            y -= 1
        else:
            return
    elif d == 3:
        if 0 <= x - 1 < N:
            dice = [dice[4], dice[1], dice[2], dice[0], dice[5], dice[3]]
            x -= 1
        else:
            return
    else:
        if 0 <= x + 1 < N:
            dice = [dice[3], dice[1], dice[2], dice[5], dice[0], dice[4]]
            x += 1
        else:
            return

    print(dice[0])

    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5], board[x][y] = board[x][y], 0


dice[5] = board[x][y]

for i in direction:
    roll(i)