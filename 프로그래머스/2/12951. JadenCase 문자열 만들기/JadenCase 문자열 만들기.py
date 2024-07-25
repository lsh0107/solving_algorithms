def solution(s):
    strings = list(s.split(' '))
    ans = []
    for i in range(len(strings)):
        if strings[i]:
            ans.append(strings[i][0].upper() + strings[i][1:].lower())
        else:
            ans.append(strings[i])
    
    return ' '.join(ans)