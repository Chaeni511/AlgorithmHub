def solution(n, computers):
    answer = 0
    q = []
    visited = [0]*n
    
    for i in range(n):
        if not visited[i]:
            q.append(i)
            visited[i] = 1
            answer += 1
            
            while q:
                j = q.pop()
                for d in range(n):
                    if j != d and not visited[d] and computers[j][d]:
                        q.append(d)
                        visited[d] = 1
    
    return answer