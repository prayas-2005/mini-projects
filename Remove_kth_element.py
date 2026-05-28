def solution(arr, k):
    new_arr = []
    for i in range(len(arr)+1):
        if i % k == 0:
            arr[i] = 0
        if i % k != 0:
            new_arr.append(i)
        
    return new_arr 
    
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# output : [1, 2, 4, 5, 7, 8, 10]
k = 3
print(solution(array, k))