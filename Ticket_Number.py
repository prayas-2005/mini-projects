def solution(n):
    s = str(n) 
    mid = len(s)/2
    first_half = sum(int(s[:mid]))
    second_half = sum(s[mid:])
    # sum_half1 = 0
    # sum_half2 = 0
    # for i in first_half:
    #     sum_half1 = sum(int(s[i]))
    print(first_half)
           
n = 1230
# 1+2 = 3+0 ->true
solution(n)