

# print(" "*0, "*", " " * 2, "*", " "*2, "*", sep="")
# print(" "*1, "*", " " * 1, "*", " "*1, "*", sep="")
# print(" "*2, "*", " " * 0, "*", " "*0, "*", sep="")

# number = 7
# start_space = 0
# space = number // 2 - 1
# flag = True
# for i in range(number):
#     if i == number//2:
#         print('*'*number)
#         flag = False
#         continue
#     print(" "*start_space, "*", " " * space, "*", " "*space, "*", sep="")
#     if i < number//2 and space == 0:
#         continue
#     if flag:
#         start_space += 1
#         space -= 1
#     else:
#         start_space -= 1
#         space += 1


month = int(input("Enter month [1-12] --> "))
day = int(input("Enter month [1-7] --> "))

days = 0
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
elif month == 2:
    year = int(input("Enter year"))
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        days = 29
    else:
        days = 28


i = 0
counter = 0
while i < days:
    if i == 0:
        print("\t"*(day-1), end="")
    i += 1
    print(i, "\t", sep='', end="")
    if (i + day - 1) % 7 == 0:
        print()
        counter += 1
        if i != 1:
            counter += 1

print()
print(counter)
