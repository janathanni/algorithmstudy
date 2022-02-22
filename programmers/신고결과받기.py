# from collections import Counter

# def solution(id_list, report, k):
#     report_list = [set() for _ in range(len(id_list))] #한 아이디가 신고한 사람들 목록
#     received_mail = [0]*len(id_list) #한 아이디가 받은 메일 수 
#     total_list = []
    
#     for i in report:
#         name, reported_name = i.split()
#         report_list[id_list.index(name)].add(reported_name)
#         total_list += list(report_list[id_list.index(name)])
        
    
#     total_report = Counter(total_list)

#     print(total_report)


#     badguys = [badguy for badguy, counts in total_report.items() if counts >= k]
    
#     print(badguys)

#     for i in badguys:
#         for j in range(len(id_list)):
#             if i in report_list[j]:
#                 received_mail[j] += 1
    
#     return received_mail

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

# print(solution(id_list, report, k))

def solution(id_list, report, k):
    report = list(set(report)) #중복 제거
    
    report_list = [[] for _ in range(len(id_list))] #한 아이디가 신고한 사람들 목록
    received_mail = [0]*len(id_list) #한 아이디가 받은 메일 수 
    reported_guy = [0]*len(id_list) #한 아이디가 받은 신고 수
    
    for i in report:
        name, reported_name = i.split()
        report_list[id_list.index(name)].append(reported_name)
        reported_guy[id_list.index(reported_name)] += 1
        
    badguy_index = [i for i, badguy in enumerate(reported_guy) if badguy>=k]
    #id_list의 index가 들어있는 거임.
    
    for i in badguy_index:
        for j in range(len(id_list)):
            if id_list[i] in report_list[j]:
                received_mail[j] += 1

    
    
    return received_mail


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))