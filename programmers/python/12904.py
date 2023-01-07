def solution(s):
    answer = 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return len(s[left + 1:right])

    if len(s) < 2 or s == s[::-1]:
        return len(s)

    for i in range(len(s)- 1):
        answer = max(answer, expand(i, i + 1), expand(i, i + 2))

    return answer

answer = solution("abacde")
print(answer)