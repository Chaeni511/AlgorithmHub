def solution(id_list, report, k):
    answer = []
    
    history  = {}
    cnt = {}
    
    for id in id_list:
        history[id] = []
        cnt[id] = 0
        
    for r in report:
        reporter, reportee = r.split()
        
        if reportee not in history[reporter]:
            cnt[reportee] += 1
        
        history[reporter].append(reportee)
    
    for id in id_list:
        history[id] = list(set(history[id]))

    for i in range(len(id_list)):
        tmp = 0
        for h in history[id_list[i]]:
            if cnt[h] >= k:
                tmp += 1
        answer.append(tmp)

    return answer   