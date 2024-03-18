def solution(priorities, location):
    answer = 0
    idx = 0
    new_priorities = []
    priorities = [(priority, idx) for idx, priority in enumerate(priorities)]
    
    high = max(priorities)[0]
    while priorities:
        if priorities[idx][0] == high:
            new_priorities.append(priorities.pop(idx))
            if priorities:
                high = max(priorities)[0]
    
            if idx >= len(priorities):
                idx = 0
            
        else:
            idx = (idx + 1) % len(priorities)
    
    for i in range(len(new_priorities)):
        if new_priorities[i][1] == location:
            return i+1
