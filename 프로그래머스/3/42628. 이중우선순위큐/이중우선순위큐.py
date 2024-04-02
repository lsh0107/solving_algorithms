def solution(operations):
    import heapq
    answer = []
    max_heap, min_heap = [], []
    cnt = 0
    for operation in operations:
        if operation[0] == 'I':
            heapq.heappush(max_heap, -int(operation[2:]))
            heapq.heappush(min_heap, int(operation[2:]))
            cnt += 1
            
        if cnt != 0 and operation[0] == 'D':
            if max_heap and operation == 'D 1':
                heapq.heappop(max_heap)
                cnt -= 1
                
            if min_heap and operation == 'D -1':
                heapq.heappop(min_heap)
                cnt -= 1
                
        if cnt == 0:
            max_heap, min_heap = [], []
            
    if cnt == 0:
        return [0, 0]
        
    answer = [-max_heap[0], min_heap[0]]
    return answer