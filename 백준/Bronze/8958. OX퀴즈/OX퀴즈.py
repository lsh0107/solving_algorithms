n = int(input())
for _ in range(n):
    ox = input()

    ans = 0
    prev = ''
    temp = []
    for a in ox:
        if a == 'O':
            temp.append(a)

        else:
            ans += len(temp)*(len(temp) + 1) // 2
            temp = []

    ans += len(temp)*(len(temp) + 1) // 2
    print(ans)