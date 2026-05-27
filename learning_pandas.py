import pandas as pd
# a = [1, 2, 3]
# data = pd.Series(a)
# print(data)
# print(data[0])

# change the index
# data = pd.Series(a, index=["x", "y","z"])
# print(data) 
# print(data["y"])

# c = {"day1": 21, "day2": 22}
# data = pd.Series(c)
# print(data)

# dataFrame = {
#     "name": ["sunil", "alexa", "Anna", "prayas", "Luca", "Mann", "Raja", "Himanshu", "Ajay", "Yogesh", "hfdhfd", "sdsds", "eqwrqe", "er3req", "dfdfdf", "kojoj", "qqwew", "yereu", "pipre", "young"],
#     "age": [22, 45, 23, 22, 45, 32, 78, 33, 23, 11, 31, 45, 44, 53, 75, 35, 11, 10, 19, 70]
# }

# print the 10 rows using head method
# data = pd.DataFrame(dataFrame)
# # print(data.head(10))
# print(data.head())


# print last 5 rows using tail method
# data = pd.DataFrame(dataFrame)
# print(data.tail(4))

# data = pd.DataFrame(dataFrame)
# print(data)
# print(data.loc[1])
# print(data.loc[[0, 1]])
# data = pd.read_csv('data.csv')
# print(data)

# print(pd.options.display.max_rows)   #max 60
# print(pd.options.display.min_rows)   #min 10

# clean duplicate format
# dataFrame = {
#     "name": ["sunil", "alexa", "Anna","Anna", "prayas", "Luca", "Mann", "Raja", "Himanshu", "Ajay", "Yogesh", "hfdhfd", "sdsds", "eqwrqe", "er3req", "dfdfdf", "kojoj", "qqwew", "yereu", "pipre", "young"],
#     "age": [22, 45, 23, 23, 22, 45, 32, 78, 33, 23, 11, 31, 45, 44, 53, 75, 35, 11, 10, 19, 70]
# }

# data = pd.DataFrame(dataFrame)
# data.drop_duplicates(inplace=True)
# print(data.to_string())


# data correlation
df = {
    "Name" : ["Prayas", "Ajay", "Sunil"],
    "Age" : [21, 34, 45],
    "courses" : ["BCA", "MCA", "BSC"],
    "City" : ["Jaipur", "Jhunjhunu", "Sikar"],
}

data = pd.DataFrame(df)
print(data.corr())


