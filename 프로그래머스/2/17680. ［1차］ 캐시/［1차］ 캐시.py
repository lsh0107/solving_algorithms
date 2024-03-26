def solution(cacheSize, cities):
    from collections import deque
    
    answer = 0
    queue = deque(maxlen=cacheSize)
    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities:
        city = city.lower()
        
        if city not in queue:
            answer += 5
            queue.append(city)

        else:
            answer += 1
            queue.remove(city)
            queue.append(city)
        
        
    return answer