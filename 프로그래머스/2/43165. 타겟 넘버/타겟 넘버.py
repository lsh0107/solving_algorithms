def solution(numbers, target):
    from collections import deque
    answer = 0
    queue = deque([(0,0)])
    while queue:
        index, curr_sum = queue.popleft()
        if index == len(numbers):
            if curr_sum == target:
                answer += 1
        
        else:
            queue.append((index + 1, curr_sum + numbers[index]))        
            queue.append((index + 1, curr_sum - numbers[index]))
            
    return answer
