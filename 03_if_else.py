# int(), float(), str(), bool(), chr()
# print("\033[31m")
# print(chr(9556),end="")
# print(chr(9552)*40,end="")
# print(chr(9559))

# print()

# print(chr(9553),end="")
# print("\033[35m",end="")
# print(" " * 15, "Pory Roku"," "*16,end="",sep="")
# print("\033[31m",end="")
# print(chr(9553))

# Користувач вводить з клавіатури відстань, витрату бензину на 100 км і вартість трьох
# видів бензину. Вивести на екран порівняльну таблицю з вартістю подорожі на різних
# видах палива.

# distance = int(input("Enter distance :: "))
# _A95_value = float(input("Enter A95 ::"))
# _A92_value = float(input("Enter A92 ::"))
# _A98_value = float(input("Enter A98 ::"))
# _A95 = float(input("Enter A95 price :: "))
# _A92 = float(input("Enter A92 price :: "))
# _A98 = float(input("Enter A98 price :: "))

# resA95 = (_A95_value/ 100) * distance * _A95
# resA92 = (_A92_value/ 100) * distance * _A92
# resA98 = (_A98_value/ 100) * distance * _A98

# print("A95 ---> " , resA95)
# print("A92 ---> " , resA92)
# print("A98 ---> " , resA98)

# a,b,c = 1,2,3
# a = b = c = 2
# +,-,*,/
# a = 100
# print(a)
# # a = a - 5
# # a = a / 2
# a -=5 # a = a - 5
# print(a) #95
# a +=5 # a = a + 5
# print(a) #100
# a *=2 # a = a * 2
# print(a) #200
# a /=2 # a = a / 2
# print(a) #100
# a %=5 # a = a % 5
# print(a) #0

# print(a,b,c)

# ==, !=, <, >, <=, >=
# a = 3
# b = 5
# print(a, " < ", b, "  ---> ", a < b) # True
# print(a, " > ", b, "  ---> ", a > b) # False
# print(a, " == ", b, " ---> ", a == b) # False
# print(a, " != ", b, " ---> ", a != b) # True
# print(a, " <= ", b, " ---> ", a <= b) # True
# print(a, " >= ", b, " ---> ", a >= b) # False

# and, or

# age = int(input("Enter your age :: "))
# # if age >= 18 and age <=30:
# if 18 <= age <= 30:
#     print("Ok")
# else:
#     print("no ok")

# numberDay = int(input("Enter number day :: "))
# if numberDay == 1:
#     print("Monday")
# elif numberDay == 2:
#     print("Tuesday")
# elif numberDay == 3:
#     print("Wednesday")
# else:
#     print("Error")

# login = input("Enter login ")
# if login == "admin":
#     password = input("Enter password ")
#     if password == "step":
#         print("Welcome")
#     else:
#         print("Error password")
# else:
#     print("Error login")