# Lv 3. 야근 지수

import heapq

def solution(n, works):
    answer = 0
    total = sum(works)
    if total > n:
        heap = []
        for i in works:
            heapq.heappush(heap, -i)

        while n > 0:
            max = heapq.heappop(heap)
            heapq.heappush(heap, max + 1)
            n -= 1

        answer = sum([work ** 2 for work in heap])

    return answer

answer = solution(4, [4, 3, 3])
print(answer)