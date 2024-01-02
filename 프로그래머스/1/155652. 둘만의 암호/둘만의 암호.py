def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    idx = 0
    for skip_word in skip:
        alpha = alpha.replace(skip_word, '')

    for char in s:
        idx = (alpha.find(char) + index) % len(alpha)
        answer += alpha[idx]
    return answer