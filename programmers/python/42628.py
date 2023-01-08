# Lv 3. 이중우선순위큐 - 힙(Heap)

import heapq

def solution(operations):
    answer = []
    heap = []
    
    for operation in operations:
        item = operation.split()
        if item[0] == 'I':
            heapq.heappush(heap, int(item[1]))
        elif item[0] == 'D' and heap:
            if item[1] == '1':
                heap.remove(max(heap))
            elif item[1] == '-1':
                heapq.heappop(heap)

    if heap:
        answer = [max(heap), heap[0]]
    else:
        answer = [0,0]

    return answer

answer = solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
print(answer)