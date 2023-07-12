

# def sumNumbers(*args):
#     for i in range(len(args)):
#         print(args[i],end='\t')
#     print()
#     return sum(args)


# result = sumNumbers(1,5,8,9,6,5,4,7,8)
# print('Sum all numbers :: ',result)

# def sum_(a, b):
#     return a+b

# def show(number):
#     print(number)


# show = lambda numb:print(numb)
# sum_ = lambda a,b:a+b

# show(333)
# print(sum_(5,3))

# numbers = [1,10,100,5,45,25,9,8,65,32,95,63]

# def doubleNumbers(list):
#     tmp = []
#     for item in list:
#         tmp.append(item * 2)
#     return tmp
# print(numbers)
# print(doubleNumbers(numbers))



# resMap = list(map(lambda x:x*2,numbers))
# print(numbers)
# print(resMap)
# print()

# def editNumber(number):
#     if number % 2 == 0:
#         return number**2
#     return number/2

# resMap = list(map(editNumber,numbers))
# print(numbers)
# print(resMap)
# print()

# def filterNumbers(item):
#     if item % 2 != 0:
#         return True
#     else:
#         return False
#     # return item % 2 != 0

# resFilter = list(filter(filterNumbers,numbers))
# print(numbers)
# print(resFilter)
# print()


# resFilter = list(filter(lambda item:item > 30 and item < 70,numbers))
# print(numbers)
# print(resFilter)
# print()


