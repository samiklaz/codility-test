def solution(N):
    # write your code in Python 3.6
    rs = len(max(format(N, 'b').strip('0').split('1')))
    return rs


print(solution(10))