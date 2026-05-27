def solution(a):
    def helper(num):
        digits = [int(d) for d in str(abs(num))]
        return max(digits) - min(digits)
    
    new_arr = [(val, i) for i, val in enumerate(a)]
   
    new_arr.sort(key=lambda x: (helper(x[0]), -x[1]))
    
    return [val for val, i in new_arr]
  
a = [152, 23, 7, 887, 243]
print(solution(a))
