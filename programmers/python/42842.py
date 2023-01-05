def solution(brown, yellow):
    answer = []

    yellow_width = yellow
    yellow_length = 1

    for i in range(1, yellow + 1):
        if yellow % i == 0 and yellow_width >= yellow_length:
            yellow_width = yellow/i
            yellow_length = i
            if (yellow_width * 2) + (yellow_length * 2) + 4 == brown:
                answer = [yellow_width + 2, yellow_length + 2]
                break

    return answer

answer = solution(8, 1)
print(answer)
