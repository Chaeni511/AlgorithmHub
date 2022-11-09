N = int(input())
classroom = [[0]*N for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N**2)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

# 자리 배치
for student in students:
    S = []
    for i in range(N):
        for j in range(N):
            blank = 0
            like = 0
            if not classroom[i][j]:
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        if classroom[ni][nj] in student[1:]:
                            like += 1
                        elif classroom[ni][nj] == 0:
                            blank += 1
                S.append((like, blank, i, j))
    S.sort(reverse=True)
    s = S[0]
    classroom[s[2]][s[3]] = student[0]

# 만족도
S = [0]*5
SS = [0, 1, 10, 100, 1000]

for student in students:
    me = student[0]
    like = student[1:]
    for i in range(N):
        for j in range(N):
            if classroom[i][j] == me:
                cnt = 0
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        if classroom[ni][nj] in like:
                            cnt += 1
                S[cnt] += 1

res = 0
for i in range(5):
    res += S[i] * SS[i]
print(res)
