array = ["abc","","aaa","a","zz"]
new_array = []
for x in range(len(array)):
    new_array.append(len(array[x]))
   
print(new_array)
new_array.sort()
print(new_array)
