# Lv 3. 입국심사 - 이분탐색

def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n

    while left < right:
        mid = (left + right) // 2
        people = 0
        for t in times:
            people += mid // t

        if people >= n:
            right = mid
        else:
            left = mid + 1

    answer = left

    return answer

answer = solution(6, [7, 10])
print(answer)