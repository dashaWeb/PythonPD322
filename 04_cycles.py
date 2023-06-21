
# i = 0
# while i < 10:
#     i+=1
#     print(i)

# i = 10
# while i > 0:
#     print(i)
#     i -=1


# i = int(input("Enter number :: "))
# print("Result :: ",end="")
# if i < 20:
#     while i <= 20:
#         print(i,end=" ")
#         i+=1
# else:
#     while i >= 20:
#         print(i,end=" ")
#         i-=1


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 1 5 9 13 ....

# i = 1
# while i <= 20:
#     print(i, end=" ")
#     i+=4


# number = int(input("Enter number "))
# if number < 1 or number > 10:
#     print("Error")
# else:
#     i = 1
#     while i < 10:
#         print(number, "x", i, "=", number * i)
#         i+=1
#     else:
#         print("Finaly")

line, i, j = 1, 1, 1

while line <= 2:
    if line == 1:
        while i <= 10:
            j = 1
            while j <= 5:
                if i == 10: 
                    print(i, 'x', j, '=', i*j, end="\t")
                else:
                    print("",i, 'x', j, '=', i*j, end="\t ")
                j += 1
            print()
            i += 1
        print()
    else:
        i = 1
        while i <= 10:
            j = 6
            while j <= 10:
                print(i, 'x', j, '=', i*j, end="\t")
                j += 1
            print()
            i += 1
    line += 1

# i,j = 2,2

# while i < 10:

#     print(i,"x",j,"=",i*j," ",end="")

#     i+=1

#     if i ==10 and j<9:

#         i=2

#         j+=1

#         print("")