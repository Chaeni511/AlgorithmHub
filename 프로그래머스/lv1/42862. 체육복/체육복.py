def solution(n, lost, reserve):
    answer = 0
    students = [0] + [1] * n + [0]
    
    for l in lost:
        students[l] -= 1
    
    for r in reserve:
        students[r] += 1
        
    for i in range(1, n+1):
        if students[i] == 0:
            if students[i-1] > 1:
                students[i-1] -= 1
                answer += 1
            elif students[i+1] > 1:
                students[i+1] -= 1
                answer += 1
        else:
            answer += 1
                
    return answer