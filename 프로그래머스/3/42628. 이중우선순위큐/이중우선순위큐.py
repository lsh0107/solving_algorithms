def solution(operations):
    import heapq
    answer = [0, 0]
    max_heap, min_heap = [], []
    cnt = 0
    for op in operations:
        order, num = op.split()
        if order == 'I':
            heapq.heappush(max_heap, -int(num))
            heapq.heappush(min_heap, int(num))
            cnt += 1
        
        elif order == 'D':
            if min_heap and int(num) == -1:
                min_ = heapq.heappop(min_heap)
                max_heap.remove(-min_)
                heapq.heapify(max_heap)
                cnt -= 1
            elif max_heap and int(num) == 1:
                max_ = heapq.heappop(max_heap)
                min_heap.remove(-max_)
                heapq.heapify(min_heap)
                cnt -= 1
        
        if cnt == 0:
            max_heap, min_heap = [], []
    
    if cnt == 0:
        return answer
    
    answer[0], answer[1] = -heapq.heappop((max_heap)), heapq.heappop(min_heap)
    return answer