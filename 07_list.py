# fruit = ['apple','plum','banana','orange']
# rnumbers = list((5,2,6,8,5,4,7))

# # print(fruit[1])
# # print(len(rnumbers))
# # print(fruit[-1::-1])

# for item in fruit[0::2]:
#     for s in item:
#         print(s,end="_")
#     print()

# print('Banana' in fruit)

# numbers = [i+2 for i in range(1,11)]
# import random
# numbers = [random.randint(20,50) for i in range(10)]
# print(numbers)
# letters = [s for s in "banana"]
# print(' '.join(letters))
# line = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et est ac mauris varius aliquet vitae vel diam. Vestibulum sit amet dignissim nisi, ac rutrum libero.'

# words = line.split('sit')
# print(words)

# colors = ['red','blue',True,555,'red','pink']
# print('Print list :: ', colors)
# colors.append('green')
# print('Print list append :: ', colors)
# colors.insert(2,'pink')
# print('Print list insert :: ', colors)
# colors.extend(['brown','violet','white'])
# print('Print list extend :: ', colors)

# colors.remove('red')
# print('Print list remove :: ', colors)
# colors.pop(3)
# print('Print list pop :: ', colors)
# colors.pop()
# print('Print list pop :: ', colors)
# # colors.clear()

# print(colors.index('red'))
# # print(colors.index('red2'))
# print(colors)
# print(colors.count('pink'))

# import random
# numbers = [random.randint(10,100) for i in range(10)]

# print('Print list :: ',numbers)
# print('Max',max(numbers))
# print('Min',min(numbers))
# print('Sum',sum(numbers))
# print('Sorted',sorted(numbers))
# print('Print list :: ',numbers)

# numbers.sort(reverse=True)
# print('Print list :: ',numbers)


# colors = ['red','green','yellow','blue','orange']
# cloneColors = colors
# print(colors is cloneColors)
# print("Colors :: ", colors)
# print("Clone Colors :: ", cloneColors)


# #cloneColors = colors.copy()
# cloneColors = list(colors)
# print('='*100)
# colors[0] = 'lime'
# print("Colors :: ", colors)
# print("Clone Colors :: ", cloneColors)


