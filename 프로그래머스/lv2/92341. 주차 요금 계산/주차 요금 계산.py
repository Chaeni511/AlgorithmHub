import math

def solution(fees, records):
    answer = []
    rec = {}
    
    dt, df = fees[0], fees[1]
    at, af = fees[2], fees[3]
    
    for record in records:
        time_tmp, plate, status = record.split()
        h, m = map(int, time_tmp.split(":"))
        time = h * 60 + m
        if plate in rec:
            rec[plate].append(time)
        else:
            rec[plate] = [time]

    for r in rec:
        if len(rec[r]) % 2:
            rec[r].append(23 * 60 + 59)
        
        rec[r] = pay(rec[r], df, dt, af, at)
    
    for k, v in sorted(rec.items()):
        answer.append(v)
        
    return answer

def pay(infos, df, dt, af, at):
    res = 0
    minute = 0
    i = 0
    
    while i < len(infos):
        minute += infos[i+1] - infos[i]
        
        i += 2
        
    res += df

    if minute - dt > 0:
        res += math.ceil((minute - dt) / at) * af
        
    return res
        