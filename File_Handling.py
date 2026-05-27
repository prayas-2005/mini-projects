# Read the file
# f = open(r"D:\python learning\demo.txt", "r")
# data = f.read()
# print(data)
# print("file name : ", f.name)
# print("file mode: ",f.mode)
# print("Closed ? :", f.closed)
# f.close()


# writing the file
# f = open("D:\python learning\demo.txt", "w")
# f.write("Hello, welcome to the pyhton program.")
# with open("D:\python learning\hello.txt", "w") as file:
#     file.write("welcome to the tutorials point!\n")
#     file.write("welcome to the coding life!\n")

# print("file written successfully!")


# read the content
# with open("D:\python learning\hello.txt","r") as file:
#     data = file.read()
#     print(data)

# deleting the file
# import os
# os.remove("D:\python learning\demo.txt")

# check the file exist or not
# import os
# if os.path.exists("D:\python learning\demo.txt"):
#     print("The path is exists!")
# else:
#     print("The path does not exists!")



# create new file
# with open("D:\python learning\hello.txt", "w") as file:
#     file.write("Hello\n")
#     file.write("Welcome to the apna college\n")
    

# Exception Handling
# a = 14
# b = 0
# try:
#     c = a/b
#     print(c)
# except:
#     print("division by zero")

# a = 14
# try:
#     c = a/0
#     print(c)
# except ZeroDivisionError:
#     print("division by zero")
# except ValueError:
#     print("Enter a valid number!")
# else:
#     print("Result is : ", c)
# finally:
#     print("Execution completed!")


# try:
#     c = int("str")
#     z = 1/c
#     print(z)
# except ValueError:
#     print("Not Valid!")
# except ZeroDivisionError:
#     print("divsion not possible!")

# a = ["10", "twenty", 30]
# try:
#     t = int(a[0]) + int(a[1])
# except ValueError as e:
#     print("Error ",e)
# except IndexError:
#     print("Index out of range!")