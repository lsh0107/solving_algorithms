def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if (idx+1) <= citation:
            answer = idx + 1
        else:
            break
    return answer
