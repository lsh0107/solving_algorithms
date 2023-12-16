def solution(s, n):
    answer = ''
    
    for char in s:
        if char != ' ':
            if char.islower() and ord(char) + n > 122:
                answer += chr(ord(char)+n-26)
            elif char.islower() and ord(char) + n <= 122:
                answer += chr(ord(char)+n)
            
            elif char.isupper() and ord(char) + n > 90:
                answer += chr(ord(char)+n-26)
            elif char.isupper() and ord(char) + n <= 90:
                answer += chr(ord(char)+n)
        else:
            answer += ' '
    return answer