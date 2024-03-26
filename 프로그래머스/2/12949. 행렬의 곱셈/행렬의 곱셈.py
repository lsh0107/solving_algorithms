def solution(arr1, arr2):
    answer = []
    for k in range(len(arr1)):
        temp = []
        for i in range(len(arr2[0])):
            num = 0
            for j in range(len(arr2)):
                num += arr1[k][j]*arr2[j][i]
            temp.append(num)
        answer.append(temp)
    return answer
