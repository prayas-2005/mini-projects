def solution(text):
    text_array = text.split(', ')
    length = []
    for i in range(len(text_array)):
        len_element = len(text_array[i])
        length.append(len_element)
    
    return max(length)
    
text = "Ready, steady, go!"
print(solution(text))