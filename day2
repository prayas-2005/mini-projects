def solution(time):
    # using mapping function
    h, m = map(int, time.split(":"))   
    if ( 0<=h<=24) and (0<=m<=59):
        return True
    else:
        return False
    
    
    # using split method
    result = time.split(":")
    h = int(result[0])
    m = int(result[1])
    if (0<=h<=23) and (59>=m>=0):
        return True
    else:
        return False
    
    
    # using slicing method
    h = int(time[0:2])
    m = int(time[3:5])
    
    if (0<=h<=23) and (59>=m>=0):
        return True
    else:
        return False
     
time = (str)(input("Enter the time : "))
print(solution(time))
