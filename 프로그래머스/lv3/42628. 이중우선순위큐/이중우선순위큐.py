from heapq import heappush, heappop

def solution(operations):
    answer = []
    hq = []
    
    for operation in operations:
        command, num = operation.split()

        if command == "I":
            heappush(hq, int(num))
        elif hq:
            if int(num) == 1:
                hq = hq[:-1]
            else:
                heappop(hq)
    
    if hq:
        answer = [max(hq), min(hq)]
    else: 
        answer = [0, 0]
        
    return answer