obj = ["username", "id", "xp"]
users = [
    ["warrior", "1", "1050"],
    ["Ninja", "21", "995"],
    ["recruit", "3", "995"]
]

users.append(obj)
# print(users)
new_arr = []
for i in range(len(users)):
    new_arr.append(users[i][0])

new_arr.remove("username")
new_arr.sort(reverse=False)
print(new_arr)