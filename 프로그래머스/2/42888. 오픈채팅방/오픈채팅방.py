def solution(record):
    answer = []
    record_v2 = []
    for rec in record:
        record_v2.append(rec.split(' '))

    dic = {rec.split()[1]:rec.split()[2] for rec in record if rec.split()[0] != 'Leave'}
    
    for rec in record_v2:
        status = rec[0]

        if status == 'Enter':
            answer.append(dic[rec[1]] + '님이 들어왔습니다.')
        
        if status == 'Leave':
            answer.append(dic[rec[1]] + '님이 나갔습니다.')

    return answer
