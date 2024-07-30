def solution(scoville, K):
    import heapq
    ans = 0
    heapq.heapify(scoville)
    while True:
        temp = 0
        not_spicy1 = heapq.heappop(scoville)
        if not_spicy1 < K:
            not_spicy2 = heapq.heappop(scoville)
            heapq.heappush(scoville, not_spicy1 + not_spicy2*2)
            ans += 1
        elif not_spicy1 >= K:
            return ans
        
        if len(scoville) == 1 and scoville[0] < K:
            break
        
    return -1
        