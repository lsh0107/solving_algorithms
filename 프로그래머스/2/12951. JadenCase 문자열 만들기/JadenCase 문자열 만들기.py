def solution(s):
    words = s.split(' ')
    ans = [word[0].upper() + word[1:].lower() if word else word for word in words]
    return ' '.join(ans)
