n = int(input())

for _ in range(n):
    h, w, N = map(int, input().split())
    H, W = 0, 1
    if N % h == 0:
        H += h
        W = N // h
    else:
        H = N % h
        W = N // h + 1

    H = str(H)
    if W < 10:
        W = '0' + str(W)
    else:
        W = str(W)

    print(H+W)