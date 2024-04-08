def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    while True:
        _min1 = heapq.heappop(scoville)
        if _min1 >= K:
            return answer
        
        else:
            _min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, _min1 + _min2*2)
            answer += 1
            
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return answer