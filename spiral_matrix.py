def solution(n):
    # curr_num = 1
    # for r in range(n):
    #     for c in range(n):
          
    matrix = [[0] * n for _ in range(n)]
    
    # Define the initial boundaries
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    # Start filling numbers from 1 to N * N
    current_num = 1
    
    while top <= bottom and left <= right:
        # 1. Move left to right across the top row
        for col in range(left, right + 1):
            matrix[top][col] = current_num
            current_num += 1
        top += 1  # Move the top boundary down
        
        # 2. Move top to bottom down the right column
        for row in range(top, bottom + 1):
            matrix[row][right] = current_num
            current_num += 1
        right -= 1  # Move the right boundary left
        
        # 3. Move right to left across the bottom row
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = current_num
            current_num += 1
        bottom -= 1  # Move the bottom boundary up
        
        # 4. Move bottom to top up the left column
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = current_num
            current_num += 1
        left += 1  # Move the left boundary right
        
    return matrix  

n = 3
print(solution(n))

# [[1, 2, 3]
# ,[8, 9, 4],
# [7, 6, 5]]