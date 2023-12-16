def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()

    for money in d:
        if answer + money <= budget:
            answer += money
            cnt += 1
        

    return cnt