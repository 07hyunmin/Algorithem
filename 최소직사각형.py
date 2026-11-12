def solution(sizes):
    answer = 0
    max = 0
    min = 0
    for i in range(len(sizes)):
        m = sizes[i][0]
        s = sizes[i][1]
        if m > s:
            lo = m
            sh = s
        else:
            lo = s
            sh = m
        if max < lo:
            max = lo
        if min < sh:
            min = sh    
    answer = max * min
    return answer

print(solution([[12,8],[10,3]]))