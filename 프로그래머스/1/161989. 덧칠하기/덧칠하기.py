def solution(n, m, section):
    answer = 0
    covered = 0

    while section:
        start = section[0]

        if start >= covered:
            covered = start + m
            answer += 1
            section.pop(0)
        else:
            section.pop(0)

    return answer