import sys

R, S = map(int, sys.stdin.readline().split())
before = [list(sys.stdin.readline().strip()) for _ in range(R)]

fall = R

for j in range(S):
    flag1 = False
    flag2 = False
    s = e = 0
    for i in range(R-1, -1, -1):

        if before[i][j] == "X":
            s = i
            flag1 = True
            break

        elif before[i][j] == "#" and before[i-1][j] == ".":
            e = i-1
            flag2 = True


    if flag1 and flag2 and e - s < fall:
        fall = e - s

after = [["."] * S for _ in range(R)]

for i in range(R):
    for j in range(S):
        if before[i][j] == "#":
            after[i][j] = "#"
        elif before[i][j] == "X":
            after[i+fall][j] = "X"

for i in range(R):
    print("".join(after[i]))
