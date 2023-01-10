# Lesson 3. Time Complexity - PermMissingElem

def solution(A):
    answer = 0
    count = len(A)
    if count == 0:
        answer = 1
    else:
        numbers = list(range(1,count+2))
        answer = (set(numbers) - set(A)).pop()

    return answer

answer = solution([1,2,3,4,5,6,7,8,9,10,12,13,14,15])
print(answer)