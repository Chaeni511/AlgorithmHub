from collections import deque

N = int(input())
buffer = deque(maxlen=N)

while True:
    packet = int(input())
    if packet == -1:
        break

    if packet == 0 and buffer:              # packet이 0이고(처리) buffer가 비어 있지 않을 때
        buffer.popleft()
    elif packet != 0 and len(buffer) < N:   # buffer가 꽉 차지 않았을 때
        buffer.append(packet)

if buffer:                              # buffer가 비어 있지 않으면
    print(' '.join(map(str, buffer)))
else:                                   # buffer가 비어 있으면
    print('empty')