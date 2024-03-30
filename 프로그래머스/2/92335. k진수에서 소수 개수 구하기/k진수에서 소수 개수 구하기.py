def solution(n, k):
    answer = 0
    r = 0
    num = ''
    numbers = []
    while n > 0:
        r = n % k
        n = n // k
        num = str(r) + num

    s = ''
    for i in num:
        if i != '0':
            s += i
        else:
            numbers.append(s)
            s = ''
    numbers.append(s)
    
    answer_copy = numbers.copy()
    for i in numbers:
        if i == '' or i == '1':
            answer_copy.remove(i)
    
    for n in answer_copy:
        if is_prime(n):
            answer += 1
    
    return answer

def is_prime(n):
    n = int(n)
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True