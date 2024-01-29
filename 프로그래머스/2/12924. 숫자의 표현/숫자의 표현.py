def solution(n):
    answer = 0
    t = 0
    num = 0
    sum_num = 0

    while True:
        num += 1
        sum_num += num
        
        if sum_num >= n:
            if sum_num == n:
                answer += 1
            t += 1
            num = t
            sum_num = 0
        
        if num > n:
            break

    return answer