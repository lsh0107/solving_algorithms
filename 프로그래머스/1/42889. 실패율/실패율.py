def solution(N, stages):
    # 1 <= N <= 500
    # 1 <= stages <= 200,000
    # stages안에 각각의 stage: 1 <= stage <= N + 1
    answer = []
    challenge = len(stages)
    for i in range(1, N+1):
        fail = stages.count(i) #현재 스테이지에 머문 플레이어
        if challenge == 0:
            failure = 0
        else:
            failure = fail/challenge
        answer.append((i, failure))
        challenge = challenge - fail
    answer = sorted(answer, key=lambda x: (-x[1], x[0]))
    answer = [order[0] for order in answer]
    return answer