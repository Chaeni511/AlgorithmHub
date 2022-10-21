N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0]))

cnt = 1
i = 0
while i < N:
    for j in range(i+1, N):
        if meeting[j][0] >= meeting[i][1]:
            i = j
            cnt += 1
            break
    else:
        break
print(cnt)