


def showRect(side,symbol = '*',flag = False):
    if flag:
        for i in range(side):
            print((symbol+' ')*side)
    else:
        for i in range(side):
            if i == 0 or i == side - 1:
                print((symbol+' ')*side)
                continue

            print(symbol,' '*(side * 2 - 3),symbol,sep='')
            

showRect(10,'+',False)

def multRange(start,end):
    if start > end:
        start,end = end,start

def numberOfDigit(number):
    counter = 0
    while number != 0:
        number //=10
        counter+=1
    return counter
# 212458
# while number{212458} != 0:
#         number //=10 #number = number{212458} // 10 --> 21245
#         counter+=1 {0 + 1 --> 1}
# while number{21245} != 0:
#         number //=10 #number = number{21245} // 10 --> 2124
#         counter+=1 {1 + 1 --> 2}
# while number{2124} != 0:
#         number //=10 #number = number{2124} // 10 --> 212
#         counter+=1 {2 + 1 --> 3}
# while number{212} != 0:
#         number //=10 #number = number{212} // 10 --> 21
#         counter+=1 {3 + 1 --> 4}
# while number{21} != 0:
#         number //=10 #number = number{21} // 10 --> 2
#         counter+=1 {4 + 1 --> 5}
# while number{2} != 0:
#         number //=10 #number = number{2} // 10 --> 0
#         counter+=1 {5 + 1 --> 6}
# while number{0} != 0:

print(numberOfDigit(212458))
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# 123321
# 2332

def checkPalindrom(number):
    length = numberOfDigit(number)
    for i in range(length//2):
        size = numberOfDigit(number)
        first = number // (10 ** (size - 1))
        last = number % 10
        print(first,last)
        if first != last:
            return False
        number = (number % (10 ** (size - 1))) // 10
    return True   


print(checkPalindrom(12354321))

