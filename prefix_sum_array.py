# a = [1, 2, 3, 4]
# sum = []
# s = 0
# for i in range(len(a)):
#     s = s + a[i]
#     sum.append(s)
#     i = i + 1
# print(sum)


        
# def solution(word1, word2):
#      set1 = set(word1) 
#      set2 = set(word2)
     
#      x = set1 - set2
#      y = set2 - set1
     
#      return "".join(sorted(x)), "".join(sorted(y))
       
# word1 = "program"
# word2 = "develop"
# print(solution(word1, word2))




# def solution(a, b):
#     result = set()
#     for i in range(len(a)):
#         for j in range(len(b)):
#             m = a[i] * b[j]
#             s = a[i] + b[j]
#             rem = (m%s)
#             if rem == 0:
#                 print("(",a[i],",",b[j],")","=",a[i] + b[j])
#                 result.add(a[i]+b[j])
#             j = j + 1 
#         i  = i + 1
#     return result

# a = [4, 5, 6, 7, 8]
# b = [8, 9, 10, 11, 12]
# print(solution(a,b))


   
      
