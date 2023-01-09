# Lesson 2. Arrays - OddOccurrencesInArray

def solution(A):
    answer = 0
    A.sort(reverse=True)

    while A:
        if len(A) == 1:
            answer = A[0]
            break

        num1 = A.pop()
        num2 = A.pop()
        if num1 != num2:
            answer = num1
            break

    return answer

answer = solution([5,1,3,2,5,3,4,4,2])
print(answer)

