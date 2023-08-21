
# import json
# students = [
#     {'name':'Valeria','lastname':'Dokukina','rating':11.9,'group':'F31','birthdate':'20.01.05','email':'lera2005olex@gmail.com','phone':'+380639290342'},
#     {'name':'Valeria2','lastname':'Dokukina','rating':11.9,'group':'F31','birthdate':'20.01.05','email':'lera2005olex@gmail.com','phone':'+380639290342'},
#     {'name':'Valeria3','lastname':'Dokukina','rating':11.9,'group':'F31','birthdate':'20.01.05','email':'lera2005olex@gmail.com','phone':'+380639290342'}
# ]

# line = json.dumps(students)
# print(type(line))
# print(line)

# obj = json.loads(line)
# print(type(obj))
# print(obj)


# obj = ''
# with open('17_file/dict.txt','r') as file:
#     obj = file.read()
# print(dict(obj))
# print(type(student_1))



# print('Print student :: ',student_1,'\n')
# student_1['visited'] = 96
# print('Print student :: ',student_1,'\n')
# del student_1['phone']
# print('Print student :: ',student_1,'\n')

# student_1.popitem()
# print('Print student :: ',student_1,'\n')
# student_1.pop('email')
# print('Print student :: ',student_1,'\n')


# for key in student_1.keys():
#     print(f'[{key}] - {student_1[key]}')
# print()

# for value in student_1.values():
#     print(value)
# print()

# for key,value in student_1.items():
#     print(f'{key} --> {value}')



import requests
import json

# result = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
# obj = json.loads(result.content)

# for item in obj:
#     for key,value in item.items():
#         print(f'{key} : {value}')
# url = 'https://t3.ftcdn.net/jpg/02/46/14/48/360_F_246144813_VSYaSoJgpD90TY566bpXRLTPCIjnD1SY.jpg'
# img = requests.get(url)
# with open('17_file/1.jpg','wb') as file:
#     file.write(img.content)

url = 'https://pixabay.com/api/?key=14304821-db198647e0592cf253911c94a&image_type=vector&category=music'
images = requests.get(url).json()

images = images['hits']
counter = 1
for img in images:
    pict = requests.get(img['webformatURL'])
    with open(f'17_file/img/{counter}.jpg','wb') as file:
        file.write(pict.content)
    counter+=1
