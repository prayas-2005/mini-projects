def solution(a, b):
    a.sort()
    b.sort()
    
    x = len(a)
    y = len(b)
    if x != y:
        return False
    elif x == y:
        for i in range(x):
            if a[i] != b[i]:
                return False
        return True
    
a = [1, 2, 3]
b = [2, 1, 3]
print(solution(a, b))


