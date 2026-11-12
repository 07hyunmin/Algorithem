def solution(price, money, count):
    answer = 0
    sum = 0
    a = 0
    for i in range(1, count + 1):
        sum += price * i
    answer = money - sum
    if answer < 0:
        answer *= -1
    else:
        answer = 0
    return answer

print(solution(1000, 400, 3))