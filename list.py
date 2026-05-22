list1 = [1, 2, 3, 4, 4, 5, 5, 6, 3, 2]
# print(list1)
newList = list(dict.fromkeys(list1))
print(newList)