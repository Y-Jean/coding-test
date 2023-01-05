"""
초기 풀이, timeout
def solution(people, limit):
    answer = 0
    people.sort()

    while people:
        if len(people) == 1:
            answer += 1
            break
        if people[-1] + people[0] > limit:
            answer += 1
            people.pop()
        elif people[-1] + people[0] == limit:
            answer += 1
            people.pop()
            people.pop(0)

    return answer
"""
def solution(people, limit):
    answer = 0
    front = 0
    rear = len(people) - 1
    people.sort()

    while front < rear:
        if people[front] + people[rear] > limit:
            answer += 1
            rear -= 1
        elif people[-1] + people[0] == limit:
            answer += 1
            front += 1
            rear -= 1

    return answer

answer = solution([1,4,2], [4,7,5])
print(answer)