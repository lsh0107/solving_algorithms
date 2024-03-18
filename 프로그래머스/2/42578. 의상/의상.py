def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic[clothes[i][1]].append(clothes[i][0])
        else:
            dic[clothes[i][1]] = [clothes[i][0]]
    
    tot = []
    for key, item in dic.items():
        tot.append(len(item)+1)
    
    print(tot)
    for i in range(len(tot)):
        answer = answer * tot[i]
    return answer - 1