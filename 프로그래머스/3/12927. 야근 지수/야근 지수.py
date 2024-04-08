def solution(n, works):
    import heapq
    pq = []
    answer = 0
    top = 0
    for work in works:
        heapq.heappush(pq, [-work, work])
    
    for i in range(n):
        top = heapq.heappop(pq)
        top[0] += 1
        top[1] -= 1
        heapq.heappush(pq, top)

    for j in pq:
        if j[1] > 0:
            answer += j[1]**2
            
    return answer