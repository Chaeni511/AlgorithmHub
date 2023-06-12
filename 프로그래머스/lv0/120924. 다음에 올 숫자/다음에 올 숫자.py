def solution(common):
    d = common[1] - common[0]
    
    if common[1] + d == common[2]:
        return common[-1] + d
    else:
        return common[-1] * (common[1] / common[0])
#     if not int(AS):
#         return common[-1] + AS
    
#     end = len(common)
#     if len(common) > 10:
#         end = 10
        
#     for i in range(end-1):
#         if common[i] + AS != common[i+1]:
#             return common[-1] * AS
#     else:
#         return common[-1] + AS

