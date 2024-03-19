def solution(bridge_length, weight, truck_weights):
    from collections import deque
    answer = 0
    time = deque()
    onbridge = deque()
    passed = []
    length = len(truck_weights)
    while True:
        answer += 1
        if time and time[0] == bridge_length:
            passed.append(onbridge.popleft())
            time.popleft()
            
        if truck_weights and sum(onbridge) + truck_weights[0] <= weight:
            onbridge.append(truck_weights.pop(0))
            time.append(0)
        
        for i in range(len(onbridge)):
            time[i] += 1
        
        if len(passed) == length:
            break
    
    return answer