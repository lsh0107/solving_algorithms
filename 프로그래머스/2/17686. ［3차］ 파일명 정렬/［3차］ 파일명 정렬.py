def solution(files):
    answer = []
    a = []
    for file in files:
        head = ''
        number_check = 0
        number = ''
        tail = ''
        flag = True
        for i in range(len(file)):
            if flag and not file[i].isnumeric():
                if file[i].isalpha() or (" " or "." or "-"):
                    head += file[i]
            elif file[i].isnumeric() and number_check < 100000:
                number += file[i]
                number_check = int(number)
                flag = False
            else:
                tail += file[i:]
                break
        answer.append([head, number, tail])
    
    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))

    for ans in answer:
        a.append(''.join(ans))
    return a