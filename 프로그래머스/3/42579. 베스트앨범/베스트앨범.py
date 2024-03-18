def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(plays)):
        if genres[i] in dic:
            dic[genres[i]].append((plays[i], i))
        else:
            dic[genres[i]] = [(plays[i], i)]
    
    print(dic)
    order = {key: sum(val[0] for val in values) for key, values in dic.items()}
    print(order)
    order = sorted(order.keys(), key=lambda x: order[x], reverse=True)
    print(order)
    
    for genre in order:
        dic[genre].sort(key=lambda x: (-x[0], x[1]))
        for i in range(min(len(dic[genre]),2)):
            answer.append(dic[genre][i][1])
            
    return answer


# print(solution(["classic","pop","classic","classic","jazz","pop","Rock","jazz"],[500, 600, 150, 800, 1100, 2500, 100, 1000]))
#[5, 1, 4, 7, 3, 0, 6]

