def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],
              [4,5,6],
              [7,8,9],
              ['*',0,'#']]
    start_left = keypad[3][0]
    start_right = keypad[3][2]

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            start_left = num
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            start_right = num
            answer += 'R'

        elif num == 2 or num == 5 or num == 8 or num == 0:
            for key in keypad:
                if start_left in key:
                    left_dy = keypad.index(key)
                    left_dx = key.index(start_left)
                
                if start_right in key:
                    right_dy = keypad.index(key)
                    right_dx = key.index(start_right)
                
                if num in key:
                    num_dy = keypad.index(key)
                    num_dx = key.index(num)
            
            dist_left = abs(num_dx - left_dx) + abs(num_dy-left_dy)
            dist_right = abs(num_dx - right_dx) + abs(num_dy - right_dy)
            
            if dist_right < dist_left:
                start_right = num
                answer += 'R'
            
            elif dist_left < dist_right:
                start_left = num
                answer += 'L'
            
            else:
                if hand == 'right':
                    start_right = num
                    answer += 'R'
                else:
                    start_left = num
                    answer += 'L'

    return answer