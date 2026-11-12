def solution(phone_number):
    answer = '*' * int(len(phone_number) - 4)
    answer += str(phone_number[-4:])
    
    return answer

print(solution("01012345678"))