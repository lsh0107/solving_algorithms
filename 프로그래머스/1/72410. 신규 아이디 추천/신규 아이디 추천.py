def solution(new_id):
    answer = ''
    #1
    new_id = new_id.lower()
    
    #2
    id = ''
    for char in new_id:
        if char != '-' and char != '_' and char != '.' and not char.isalnum():
            id += ''
        else:
            id += char
    
    #3
    ans = [id[0]]
    for idx in range(1, len(id)):
        if ans[-1] == '.' and id[idx] == '.':
            pass

        else:
            ans.append(id[idx])
    
    #4
    answer =  ''.join(ans)
    if answer and (ans[-1] == '.' or answer[0] == '.'):
        if answer and answer[0] == '.':
            answer = answer[1:]
        
        if answer and answer[-1] == '.':
            answer = answer[:-1]
    
    #5
    if not answer:
        answer += 'a'
    
    #6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
        
    return answer