def solution(s):
    S = s
    start = s[0]
    char = []
    x_count = 0
    not_x_count = 0
    idx = 0
    while s:
        if start == s[idx]:
            #x = s[i]
            x_count += 1
            idx += 1
        elif start != s[idx]:
            #not_x = s[i]
            not_x_count += 1
            idx += 1

        if x_count == not_x_count:
            char.append(s[:x_count + not_x_count])
            if ''.join(char) == S:
                break
            if x_count + not_x_count < len(s):
                s = s[x_count + not_x_count:]
                start = s[0]
                x_count, not_x_count, idx = 0, 0, 0

        elif x_count + not_x_count == len(s):
            char.append(s)
            s = ''

    return len(char)