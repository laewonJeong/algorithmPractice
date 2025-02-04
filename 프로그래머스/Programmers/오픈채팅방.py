def solution(records):
    answer = []
    uid_dic = {record.split()[1]: record.split()[-1] for record in records if record[0] != "L"}
    print_dic = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}

    for record in records:
        if record[0] == "C": continue
        act, uid = record.split()[0:2]
        answer.append(f"{uid_dic[uid]}님이 {print_dic[act]}")
            
    return answer
