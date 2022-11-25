# 136. single number

from typing import List

def singleNumbers(nums: List[int]) :
    result = 0
    for num in nums:
        result ^= num

    return result

answer = singleNumbers([4,1,2,1,2])
print(answer)