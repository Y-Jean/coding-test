# Lesson 3. Time Complexity - TapeEquilibrium

def solution(A):
    left = A[0]
    right = sum(A[1:])
    answer = abs(left - right)

    for i in range(1,len(A)-1):
        left += A[i]
        right -= A[i]
        answer = min(answer, abs(left - right))

    return answer

answer = solution([-2, -3, -4, -1])
print(answer)