# 브론즈 2. 블랙잭

from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sum = 0

for i, j, k in permutations(nums, 3):
    if (i+j+k > M):
        continue
    else:
        sum = max(sum, i+j+k)
print(sum)

# 다른 풀이
"""
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if (nums[i] + nums[j] + nums[k] > M):
                continue
            else:
                sum = max(sum, nums[i] + nums[j] + nums[k])
"""
