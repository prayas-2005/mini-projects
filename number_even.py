def solution(n):
    s = str(n)
    for i in range(len(s)):
          rem = int(s[i]) % 2
          if rem != 0:
              return False 
    return True
            
n = (int)(input("Enter the number : "))
print(solution(n))