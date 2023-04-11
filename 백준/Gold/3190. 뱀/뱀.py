from collections import deque

    # 동  북  서  남
di = [0 ,-1, 0, 1]
dj = [1, 0, -1, 0]

N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
L = int(input())
dir = []
for _ in range(L):
    x, c = input().split()
    dir.append((int(x), c))
d = 0

hr = hc = sec = 0
snake = deque()
snake.append((0, 0))
flag = True

def func1():
    global hr, hc, sec, d, flag
    for x, c in dir:
        for i in range(sec, x):
            hr += di[d]
            hc += dj[d]
            sec += 1
            if hr < 0 or hr >= N or hc < 0 or hc >= N or (hr, hc) in snake:
                flag = False
                return
            snake.append((hr, hc))

            if arr[hr][hc] == 0:
                snake.popleft()
            else:
                arr[hr][hc] = 0

        if c == 'L':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4


def func2():
    global hr, hc, sec, d
    while True:
        hr += di[d]
        hc += dj[d]
        sec += 1
        if hr < 0 or hr >= N or hc < 0 or hc >= N or (hr, hc) in snake:
            return
        snake.append((hr, hc))

        if arr[hr][hc] == 0:
            snake.popleft()
        else:
            arr[hr][hc] = 0


func1()

if flag:
    func2()

print(sec)
