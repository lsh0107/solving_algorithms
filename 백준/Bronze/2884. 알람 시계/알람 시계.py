n = list(map(int, input().split()))
h = 0
m = 0

if n[0] - 1 >= 0:
    if n[1] - 45 < 0:
        h = n[0] - 1
        m = (n[1] - 45) % 60

    else:
        h = n[0]
        m = (n[1] - 45) % 60

else:
    if n[1] - 45 < 0:
        h = (n[0] - 1) % 24
        m = (n[1] - 45) % 60

    else:
        h = n[0] % 24
        m = (n[1] - 45) % 60

print(h, m)