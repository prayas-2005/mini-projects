
n = (int)(input("Enter the child : "))
m = (int)(input("Enter the pieces of candy : "))
p = 3

div = int(m/n)
if n  > 0:
    result = int(m/n) * p
    print(result)
else:
    print("not possible")