from collections import deque

def solution(begin, target, words):
    answer = 0
    
    q = deque([(begin, 0)])
    
    if target in words:
        while q:
            this, cnt = q.popleft()

            if this == target:
                answer = cnt
                return answer

            for word in words:
                tmp = 0
                for i in range(len(this)):
                    if this[i] != word[i]:
                        tmp += 1
                    if tmp > 1:
                        break
                else:
                    q.append((word, cnt + 1))
    return answer