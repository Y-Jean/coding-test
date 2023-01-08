# Lv 2. 최솟값 만들기

def solution(A,B):
    answer = 0

    A.sort(reverse=True)
    B.sort()

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

answer = solution([1,4,2], [4,7,5])
print(answer)