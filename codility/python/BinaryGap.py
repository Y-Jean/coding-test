# Lesson 1. Iterations - BinaryGap

def solution(N):
    answer = 0
    binary_num = bin(N)[2:]

    count = 0
    for i in range(len(binary_num)):
        if binary_num[i] == '1':
            answer = max(count, answer)
            count = 0
        else:
            count += 1

    return answer

answer = solution(32)
print(answer)