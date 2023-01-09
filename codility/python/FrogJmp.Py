# Lesson 3. Time Complexity - FrogJmp

def solution(X, Y, D):
    answer = 0

    if X == Y:
        answer = 0
    else:
        answer, remainder = divmod(Y - X, D)
        if remainder != 0:
            answer += 1

    return answer

answer = solution(10, 85, 30)
print(answer)

