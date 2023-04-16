import copy


# +1 반시계 -1 시계
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
arr = copy.deepcopy(A)

ap_r1 = ap_c1 = ap_r2 = ap_c2 = 0
def ap_check():
    global ap_r1, ap_r1, ap_r2, ap_r2
    for i in range(R):
        for j in range(C):
            if A[i][j] == -1:
                ap_r1, ap_c1 = i, j
                ap_r2, ap_c2 = i+1, j
                return
ap_check()

ap_r1_or = ap_r1
ap_r2_or = ap_r2
ap_c1_or = ap_c1
ap_c2_or = ap_c2


for t in range(T):
    # 확산
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in [(ap_r1, ap_c1), (ap_r2, ap_c2)]:
                        arr[ni][nj] += A[i][j]//5
                        arr[i][j] -= A[i][j]//5

    # 공기청정기 반시계
    temp = 0
    for d in range(4):
        ii = 1
        while 0 <= ap_r1 + ii * di[d] < R and 0 <= ap_c1 + ii * dj[d] < C and (ap_r1 + ii * di[d], ap_c1 + ii * dj[d]) != (ap_r1_or, ap_c1_or):
            temp, arr[ap_r1 + ii * di[d]][ap_c1 + ii * dj[d]] = arr[ap_r1 + ii * di[d]][ap_c1 + ii * dj[d]], temp
            ii += 1

        if d == 3:
            ap_r1, ap_c1 = ap_r1_or, ap_c1_or

        else:
            ap_r1, ap_c1 = ap_r1 + (ii-1) * di[d], ap_c1 + (ii-1) * dj[d]

    temp = 0
    # 공기청정기 시계
    for d in [0, 3, 2, 1]:
        ii = 1
        while 0 <= ap_r2 + ii * di[d] < R and 0 <= ap_c2 + ii * dj[d] < C and (ap_r2 + ii * di[d], ap_c2 + ii * dj[d]) != (ap_r2_or, ap_c2_or):
            temp, arr[ap_r2 + ii * di[d]][ap_c2 + ii * dj[d]] = arr[ap_r2 + ii * di[d]][ap_c2 + ii * dj[d]], temp
            ii += 1

        if d == 1:
            ap_r2, ap_c2 = ap_r2_or, ap_c2_or
        else:
            ap_r2, ap_c2 = ap_r2 + (ii-1) * di[d], ap_c2 + (ii-1) * dj[d]

    A = copy.deepcopy(arr)

res = 0
for i in range(R):
    res += sum(arr[i])

print(res+2)