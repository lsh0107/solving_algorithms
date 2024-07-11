import sys

input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()
cnt = len(nums)
dic = {}
print(int(round(sum(nums)/cnt, 0)))
if len(nums) % 2 != 0:
    print(nums[cnt//2])

for i in nums:
    try:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    except:
        continue

new_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
val = max(new_dic, key=lambda x: x[1])[1]
if len(new_dic) > 1 and new_dic[0][1] == new_dic[1][1]:
    print(new_dic[1][0])
else:
    print(new_dic[0][0])

print(abs(nums[0]-nums[-1]))