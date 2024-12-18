def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    cur_time = 60*int(pos[:2]) + int(pos[3:])
    op_time_start = 60*int(op_start[:2]) + int(op_start[3:])
    op_time_end = 60*int(op_end[:2]) + int(op_end[3:])
    start_time, end_time = 0, 60*int(video_len[:2]) + int(video_len[3:])
    mm, ss = 0, 0
    for command in commands:
        cur_time = check_time(cur_time, op_time_start, op_time_end)
        if command == "next":
            cur_time += 10
            if cur_time >= end_time:
                cur_time = end_time
            else:
                cur_time = check_time(cur_time, op_time_start, op_time_end)
        else:
            cur_time -= 10
            if cur_time <= start_time:
                 cur_time = start_time
            else:
                cur_time = check_time(cur_time, op_time_start, op_time_end)

    if cur_time >= end_time:
        cur_time = end_time
    
    mm = cur_time//60
    ss = cur_time%60

    if mm < 10:
        mm = '0' + str(mm)
    else:
        mm = str(mm)
    
    if ss < 10:
        ss = '0' + str(ss)
    else:
        ss = str(ss)
    
    answer = mm + ":" + ss
    return answer

def check_time(cur_time, op_time_start, op_time_end):
    if cur_time >= op_time_start and cur_time <= op_time_end:
        cur_time = op_time_end
    return cur_time