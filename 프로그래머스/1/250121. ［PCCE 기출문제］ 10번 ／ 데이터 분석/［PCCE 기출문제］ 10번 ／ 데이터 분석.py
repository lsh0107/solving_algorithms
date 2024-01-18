def solution(data, ext, val_ext, sort_by):
    type = ['code', 'date', 'maximum', 'remain']
    index_1 = type.index(ext)
    index_2 = type.index(sort_by)
    answer = []
    
    for idx, d in enumerate(data):
        if d[index_1] < val_ext:
            answer.append(d)
        else: pass
    
    answer = sorted(answer, key=lambda x: x[index_2])
    
    return answer