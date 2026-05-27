import pandas as pd
# print(pd.__version__)
# df = pd.DataFrame() #creates an empty dataframe

# df['Name'] = ["Anna", "Prayas", "Sunil", "Oliva"]
# df['Age'] = [23, 34, 45, 56]
# df['City'] = ["Jaipur", "Nawalgarh", "Jhunjhnu", "Kota"]
# df['id'] = [".."]  raise value error

# data = {
#     "Name": ["prayas", "sunil", "ajay"],
#     "Age":[21, 34, 45],
#     "City":["Nawalgarh", "Jhunjhunu", "Jaipur"]
# }

# pf = pd.DataFrame(data, index=["day1","day2", "day3"])
# print(pf)

# df = pd.DataFrame(data)
# df.loc[len(df)] = ["charlie", 67, "Kota"]
# df.loc[len(df)] = ["Anna", 37, "Haldwani"]
# print(df)


# print(df)

# Adding new row in DataFrame
# new_row = pd.DataFrame([["Ajay", 35, "Nawalgarh"],["Susil",56, "Jodhpur"]], columns=["Name", "Age", "City"])
# df = pd.concat([df, new_row], ignore_index=True)

# df.loc[len(df)] = ["Charlie", 37, "America"]
# print(df)

# print("#",df)
# print(df.shape)
# print(df.info())

# drop columns
# df2 = df.drop("Age", axis=1)
# print(df2)

# drop rows
# df3 = df.drop(2, axis=0)
# print(df3)

# select data form DataFrame
# print(df['Name'])  
# print(df[['Name', 'Age']])
# print(df.loc[0])


# Filtering Data
# print(df[df['Age'] > 40])
# print(df[df['Name'] == 'Prayas'])
# print(df[df['City'] == 'Nawalgarh'])

# sorting the data in DataFrame
# print(df.sort_values(by='Age'))


# df = pd.read_csv('data.csv')

# print(df.to_string()) 


data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
# print(df[df['Duration'] == 60]) 
# print(df.head(3))
# print(df.head())
print(df.tail())
