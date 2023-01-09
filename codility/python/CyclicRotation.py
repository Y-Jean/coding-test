# Lesson 2. Arrays - CyclicRotation

def solution(A, K):
    answer = []
    if A:
        K %= len(A)

        left = A[:-K]
        right = A[-K:]

        answer = right + left

    return answer

answer = solution([], 6)
print(answer)