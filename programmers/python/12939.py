# Lv 2. 최댓값과 최솟값

def solution(s):
    nums = s.split()
    nums = list(map(int, nums))
    max = nums[0]
    min = nums[0]

    for num in nums:
        if num > max:
            max = num
        elif num < min:
            min = num

    answer = str(min) + " " + str(max)
    return answer


answer = solution("1 2 3 4")
print(answer)