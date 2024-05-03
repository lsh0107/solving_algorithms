def solution(number, k):
    answer = []
    for idx, num in enumerate(number):
        while answer and k > 0 and int(answer[-1]) < int(num):
                answer.pop()
                k -= 1
        
        if k == 0:
            answer.append(number[idx:])
            break
        
        answer.append(num)
    
    for i in range(k):
        answer.pop()
        
    return ''.join(answer)