# відкрити файл
# прочитати файл
# записати у файл
# закрити файл

# url = r'C:\Users\dev\Desktop\PythonPD322\16_file\my.txt'
# fileHandler = open(url)

# file_str = fileHandler.read()
# file_str = fileHandler.read(15)
# file_str = fileHandler.readline()
# file_str = fileHandler.readlines()
# print(file_str,'\n Type :: ', type(file_str))
# for line in file_str:
#     print(line.strip())

# for line in fileHandler:
#     print(line)

# fileHandler.close()

# with open(url) as fileHandler:
#     print(fileHandler.read())

# lines = [
#     'Fusce id dolor a ex ornare lacinia eu eu ex.\n',
#     'Nulla ullamcorper odio et tempus rhoncus.\n',
#     'Quisque quis nisi a arcu luctus luctus.\n',
# ]

# url = '16_file/write.txt'
# # with open(url, 'a') as file:
# #     counter = 1
# #     for line in lines:
# #         file.write(f'{counter}) {line}\n')
# #         counter+=1

# with open(url,'w') as file:
#     file.writelines(lines)

url = '16_file/text.txt'



# def readFile(fname):
#     with open(fname) as file:
#         return file.read()

# def replaceText(text,oldText,newText):
#     return text.replace(oldText,newText)

# def writeFile(fname,newText):
#     with open(fname,'w') as file:
#         file.write(newText)


# originWord = input('Enter word > ')
# newWord = input('Enter new word > ')

# text = readFile(url)
# replace = replaceText(text,originWord,newWord)
# writeFile(url,replace)

# url = '16_file/text.txt'
# url2 = '16_file/text2.txt'

# def readFile(fname):
#     with open(fname,encoding='utf-8') as file:
#         return file.read()
    
# def removePunct(line, marks):
#     str_ = ''
#     for ch in line:
#         if ch not in marks:
#             str_+=ch
#     return str_

# def writeFile(url,line):
#     with open(url,'w',encoding='utf-8') as file:
#         file.write(line)

# marks = '.,_-!?&—():«»'
# text = readFile(url)
# removeText = removePunct(text,marks)
# newText = ' '.join(removeText.split()[::-1])

# writeFile(url2,newText)
 
# number_1 = [11,15,16,25,48,22]

# with open('16_file/number.txt','w') as file:
#     newNumber = []
#     for i in number_1:
#         newNumber.append(str(i))
#     file.write(' '.join(newNumber))

str = '''[{"ccy":"EUR","base_ccy":"UAH","buy":"40.80000","sale":"41.80000"},{"ccy":"USD","base_ccy":"UAH","buy":"37.35000","sale":"38.05000"}]'''
