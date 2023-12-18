def solution(s):
    answer = ''
    dic = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
           'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
    strings = [char for char in s]
    char = ''

    while strings:
        if strings[0].isdigit():
            answer += strings[0]
            strings.pop(0)

        else:
            char += strings[0]
            strings.pop(0)
            if char in dic:
                answer += str(dic.get(char))
                char = ''

    return int(answer)