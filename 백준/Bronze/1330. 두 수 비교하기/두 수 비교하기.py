num = input().split()
ans = [int(x) for x in num]

if ans[0] > ans[1]:
    print(">")
elif ans[0] < ans[1]:
    print("<")
else:
    print("==")