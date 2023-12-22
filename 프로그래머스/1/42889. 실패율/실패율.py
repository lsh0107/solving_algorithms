def solution(N, stages):
    # 1 <= N <= 500
    # 1 <= stages <= 200,000
    # stages안에 각각의 stage: 1 <= stage <= N + 1
    answer = []

    for i in range(1, N+1):
        challenge, fail, failure = 0, 0, 0
        for stage in stages:
            if stage == i:
                fail += 1
                challenge += 1
            elif stage > i:
                challenge += 1
        if challenge == 0:
            failure = 0
        else: 
            failure = fail/challenge
        answer.append((i, failure))

    answer = sorted(answer, key=lambda x: (-x[1], x[0]))
    answer = [order[0] for order in answer]
    return answer