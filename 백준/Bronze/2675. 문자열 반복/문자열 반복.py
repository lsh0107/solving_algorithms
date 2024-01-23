N = int(input())
data = []
for _ in range(N):
    data.append(input().split())

answer = ''
for i in range(len(data)):
    for s in data[i][1]:
        answer += s*int(data[i][0])
    print(answer)
    answer = ''