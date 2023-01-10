# Lv 2. 예산

def solution(d, budget):
    answer = 0
    d.sort(reverse=True)

    while d:
        if budget < sum(d):
            d = d[1:]
            print(d)
        else:
            answer = len(d)
            break

    return answer

answer = solution([1, 3, 2, 5, 4], 9)
print(answer)