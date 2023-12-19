def solution(n, arr1, arr2):
    answer = []
    num = 0
    map1 = []
    map2 = []
    for i in arr1:
        temp = []
        for j in range(n):
            num = divmod(i, 2)
            i = num[0]
            temp.append(num[1])
        map1.append(temp[::-1])

    for i in arr2:
        temp = []
        for j in range(n):
            num = divmod(i, 2)
            i = num[0]
            temp.append(num[1])
        map2.append(temp[::-1])
    
    for k in range(n):
        temp = ''
        for l in range(n):
            if map1[k][l] == 1 or map2[k][l] == 1:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer