def solution(n, words):
    order, cnt = 0, 1
    prev = words[0]
    dic = {prev: 1}
    for i in range(1, len(words)):
        if i % n == 0:
            cnt += 1

        if words[i][0] == prev[-1]:
            order = i % n + 1
            
            if words[i] not in dic:
                dic[words[i]] = 1
            
            else:
                return [order, cnt]

            prev = words[i][-1]
        
        else:
            order = i % n + 1
            return [order, cnt]
        
    if max(dic.values()) == 1:
        return [0, 0]
    
    return [order, cnt]