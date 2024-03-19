def solution(k, dungeons):
    from itertools import permutations
    answer = []
    comb = []
    comb += list(permutations(dungeons, len(dungeons)))
    
    for dungeon in comb:
        curr_k = k
        cnt = 0
        for i in range(len(dungeon)):
            if curr_k < dungeon[i][0]:
                break
                
            curr_k -= dungeon[i][1]
            cnt += 1
        answer.append(cnt)
        
    return max(answer)