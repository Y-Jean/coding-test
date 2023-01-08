# Lv 2. 피보나치 수

def solution(n):
    answer = 0
    a, b = 1, 1

    for i in range(1, n):
        a, b = b, a + b

    answer = a % 1234567

    return answer

answer = solution(3)
print(answer)