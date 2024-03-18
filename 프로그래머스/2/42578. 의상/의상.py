def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic[clothes[i][1]] += 1
        else:
            dic[clothes[i][1]] = 2
    
    for key, item in dic.items():
        answer *= item
 
    return answer - 1