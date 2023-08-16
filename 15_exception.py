
# num = None
# num2 = None

# while num == None or num2 == None or num2 == 0:
#     try:
#         num = int(input('Enter number > '))
#         num2 = int(input('Enter number > '))
#         print(num / num2)
#     except ValueError:
#         print('Error value')
#     except ZeroDivisionError:
#         print('division by zero')
#     except Exception:
#         print('Exception')


# print('End .... ')
#......
# try:
#     colors = ['red','green','blue','yellow']
#     index = int(input('Enter position color > '))
#     print(colors[index])
# except IndexError:
#     print('Index error')
# except Exception:
#     print('value type error')
# else:
#     print('Good')
# finally:
#     print('finally')


# try:
#     num = int(input('Enter number > '))
#     if num < 0:
#         raise ValueError('number < 0')
#     if num > 1000000:
#         raise ValueError('number > 1000000')
#     print('Ok --> ',num)
# except ValueError as ex:
#     print(ex)

# library = [
#     ['name','author','publisher','genre',45.25,9.6],
#     ['name','author','publisher','genre',45.25,9.6],
#     ['name','author','publisher','genre',45.25,9.6],
#     ['name','author','publisher','genre',45.25,9.6],
#     ['name','author','publisher','genre',45.25,9.6],
#     ['name','author','publisher','genre',45.25,9.6],
#     ['name','author','publisher','genre',45.25,9.6],
#     ['name','author','publisher','genre',45.25,9.6],
#     ['name','author','publisher','genre',45.25,9.6],
#     ['name','author','publisher','genre',45.25,9.6],  
# ]