# Lv 1. 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(participant)):
        if i >= len(completion) or participant[i] != completion[i]:
            answer = participant[i]
            break

    return answer

answer = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
print(answer)