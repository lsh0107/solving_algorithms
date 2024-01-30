def solution(n):
    answer = n
    count_one = bin(n)[2:].count('1')
    while True:
        answer += 1
        check_num = bin(answer)[2:]
        if check_num.count('1') == count_one:
            return answer