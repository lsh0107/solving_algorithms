from collections import deque

def solution(queue1, queue2):
    answer = -1
    q1, q2 = sum(queue1), sum(queue2)
    total = q1 + q2
    if (q1+q2) % 2 != 0:
        return answer
    
    n = 0
    length = max(len(queue1), len(queue2))
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while True:
        if q1 == (total//2):
            return answer + 1
        
        if q1 > q2:
            item = queue1.popleft()
            queue2.append(item)
            q1 -= item
            q2 += item
            answer += 1
            n += 1
        
        if q1 < q2:
            item = queue2.popleft()
            queue1.append(item)
            q1 += item
            q2 -= item
            answer += 1  
            n += 1
        
        if n > length*3:
            return -1
        