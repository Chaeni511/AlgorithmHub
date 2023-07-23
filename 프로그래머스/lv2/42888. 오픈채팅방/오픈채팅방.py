def solution(records):
    answer = []
    uid_nickname = {}
    
    for record in records:
        tmp = record.split()
        
        if len(tmp) == 2:
            status, uid = tmp[0], tmp[1]
        else:
            status, uid, nickname = tmp[0], tmp[1], tmp[2]

            
        if uid not in uid_nickname:
            uid_nickname[uid] = nickname

        if status == "Change":
            uid_nickname[uid] = nickname

        else:
            if status == "Enter" and uid_nickname[uid] != nickname:
                uid_nickname[uid] = nickname
    
            answer.append((uid, status))
            
    for i in range(len(answer)):
        uid, status = answer[i][0], answer[i][1]
        msg = uid_nickname[uid] + "님이 "
        
        if status == "Enter":
            msg += "들어왔습니다."
        else:
            msg += "나갔습니다."
            
        answer[i] = msg        
            
    return answer