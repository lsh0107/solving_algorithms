def solution(n, t, m, p):
    # 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.
    dic = {}
    answer = ''
    order = 0
    for i in range(t*m):
        num = trans_num(i, n)
        if len(num) == 1:
            if order == p - 1:
                answer += num
            order = (order + 1) % m
        
        elif len(num) >= 2:
            for nu in num:
                if order == p - 1:
                    answer += nu
                order = (order + 1) % m
                
    return answer[:t]

def trans_num(num, n):
    
    t = '0123456789ABCDEF'
    number = ''
    r = 0
    while num > 0:
        r = num % n
        num = num // n
        number = t[r] + number

    if len(number) == 0:
        return '0'

    return number
