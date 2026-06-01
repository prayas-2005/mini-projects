def solution(n):
    s = str(n) 
    
    half = len(s) // 2
    first_half = sum(int(d) for d in s[:half])
    second_half = sum(int(d) for d in s[half:])
    if first_half == second_half:
        return True
    else:
        return False
    
   
n = (int)(input("Enter the number : "))
# print(solution(n))
solution(n)