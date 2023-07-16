def solution(new_id):
        
    # 1
    new_id = new_id.lower()
    
    # 2
    tmp = ''
    for i in new_id:
        if i.isalnum():
           tmp += i
        else:
            if i == '-' or i == '_' or i == '.':
                tmp += i
    new_id = tmp

    # 3
    tmp = ''
    i = 0
    while i < len(new_id):
        if new_id[i] == '.':
            tmp += new_id[i]
            i += 1
            for j in new_id[i:]:
                if j != '.':
                    break
                else :
                    i += 1
            
        else: 
            tmp += new_id[i]
            i += 1
    new_id = tmp
    
    # 4
    if new_id[0] == '.':
        new_id = new_id[1:]
        
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    # 5
    if not new_id:
        new_id = 'a'
    
    # 6
    if len(new_id) > 15:
        new_id = new_id[:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]
            
    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
    return new_id
