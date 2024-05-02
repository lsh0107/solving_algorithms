def solution(order):
    answer = 0
    con = [i for i in range(len(order), 0, -1)]
    stack = []
    i = 0
    while True:
        if con and order[i] == con[-1]:
            con.pop()
            i += 1
            answer += 1

        elif con and con[-1] < order[i]:
            stack.append(con.pop())
        
        elif stack and stack[-1] == order[i]:
            stack.pop()
            answer += 1
            i += 1

        else:
            if  not stack or (order[i] != stack[-1] and order[i] != con[-1]):
                return answer