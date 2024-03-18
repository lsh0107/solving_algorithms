def solution(progresses, speeds):
    answer = []
    done = []
    while progresses:
        if progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        
        if progresses[0] >= 100:
            while progresses and progresses[0] >= 100:
                done.append(progresses.pop(0))
                speeds.pop(0)
            
            
            answer.append(len(done))
            done = []
        
    return answer
