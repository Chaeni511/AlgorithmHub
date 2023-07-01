from itertools import permutations


def check():
    press = 0
    button = origin[:]
    for i in range(1, N):
        if button[i-1] != target[i-1]:
            press += 1
            for j in range(i-1, i+2):
                if j < N:
                    button[j] = 1 - button[j]

    if button == target:
        return press
    else:
        return 1e9


N = int(input())
origin = list(map(int, list(input())))
target = list(map(int, list(input())))

# 첫번째 스위치를 누르지 않는 경우
res = check()

# 첫번째 스위치를 누르는 경우
origin[0] = 1 - origin[0]
origin[1] = 1 - origin[1]

res = min(res, check() + 1)

if res == 1e9:
    print(-1)
else:
    print(res)
