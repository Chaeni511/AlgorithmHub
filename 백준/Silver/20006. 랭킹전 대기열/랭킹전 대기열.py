import sys

p, m = map(int, sys.stdin.readline().split())
rooms = []

for _ in range(p):
    flag = True
    lv, nm = sys.stdin.readline().split()
    lv = int(lv)
    for room in rooms:
        if len(room) == m:
            continue
        if room[0][0] - 10 <= lv <= room[0][0] + 10:
            flag = False
            room.append([lv, nm])
            break
    if flag:
        rooms.append([[lv, nm]])
    # if not room:
    #     room.append([(lv, nm)])
    # else:
    #     for i in range(len(room)):
    #         if len(room[i][0]) < m and room[i][0][0] - 10 <= lv <= room[i][0][0] + 10:
    #             room[i].append((lv, nm))
    #             break
    #     else:
    #         room.append([(lv, nm)])

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    room.sort(key=lambda x: x[1])
    for l, n in room:
        print(l, n)
    # for j in range(len(room[i])):
    #     print(' '.join(map(str, room[i][j])))
