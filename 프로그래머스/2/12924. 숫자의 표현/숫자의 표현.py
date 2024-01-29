def solution(n):
    answer = 0
    t = 0
    num = 0
    sum_num = 0

    while True:
        if n in [1, 2] or num == n//2 + 1:
            answer += 1
            break

        num += 1
        sum_num += num
        if sum_num == n:
            t += 1
            num = t
            sum_num = 0
            answer += 1
        
        elif sum_num > n:
            t += 1
            num = t
            sum_num = 0
        

    return answer
