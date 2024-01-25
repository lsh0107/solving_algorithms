def solution(friends, gifts):
    answer = [0 for name in range(len(friends))]
    gift_count = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for gift in gifts:
        giver, receiver = gift.split()  # "주는 사람 받는 사람"을 분리하여 저장
        giver_idx = friends.index(giver)
        receiver_idx = friends.index(receiver)
        gift_count[giver_idx][receiver_idx] += 1  # 주는 사람과 받는 사람 간의 선물 횟수를 1 증가

    for i in range(len(gift_count)):
        for j in range(i + 1, len(gift_count[i])):
            give = gift_count[i][j]
            receive = gift_count[j][i]

            if give != receive and (give > 0 or receive > 0):
                if give > receive:
                    answer[i] += 1
                else:
                    answer[j] += 1
            
            else:
                give_score = sum(gift_count[i])
                receive_score = sum(gift_count[j])

                for k in range(len(gift_count)):
                    give_score -= gift_count[k][i]
                    receive_score -= gift_count[k][j]
                
                if give_score > receive_score:
                    answer[i] += 1
                elif give_score < receive_score:
                    answer[j] += 1
                    
    return max(answer)