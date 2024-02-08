def solution(k, tangerine):
    answer = 0
    count = [0]*max(tangerine)
    
    for idx in tangerine:
        count[idx-1] += 1
    
    count = sorted(count, reverse=True)

    for i in count:
        k -= i
        answer += 1
        if k <= 0:
            break
    
    return answer