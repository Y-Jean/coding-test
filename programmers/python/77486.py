# Lv 3. 다단계 칫솔 판매

def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    dict = {}

    for i, e in enumerate(enroll):
        dict[e] = i # i = 번호, e = 이름

    for s, a in zip(seller, amount):
        money = a * 100 # 수량을 금액으로

        while s != "-" and money > 0:
            idx = dict[s] #dict에서 저장했던 입력받은 순서를 이름으로 찾기
            re_money = money//10
            answer[idx] += money - re_money
            money = re_money
            s = referral[idx] #상위 찾아서 반복

    return answer

answer = solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], #enroll
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], #referral
    ["sam", "emily", "jaimie", "edward"], #seller
    [2, 3, 5, 4] #amount
)
print(answer)