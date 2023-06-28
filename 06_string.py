
# for i in range(1000000):
#     print(i, ' --> ', chr(i), end='\t')
#     if i % 10 == 0:
#         print()

# print(ord('a'))

# line = "Lorem ipsum dolor"

# print(id(line), line)
# line += " !!!!! "
# print(id(line), line)
# # line[3] = 'b'
# print(len(line))
# print(line[3:len(line)])
# print(line[3:10:2])
# print(line[-10:-2])

# number_1 = 2
# number_2 = 5
# # 2 + 5 = 7
# # example = number_1, " + ", number_2, " = ", number_1 + number_2
# # print(type(example))
# example = '{} + {} = {}'.format(number_1, number_2, number_1 + number_2)
# print(example)
# print(type(example))

# # name lorem name ipsum age
# name = 'Petro'
# age = 22
# example = '{1} {0} {1} lorem {0} ipsum {1} {0}'.format(name, age)
# print(example)


# line_1 = 'lorem/ \\ ipsum'
# line_2 = "I \n\tlove Python"
# line_3 = '''
#             I
#                 Love
#                         Python
#                                 !!!!!
#         '''
# # \n - Enter

# line_4 = '\\n - Enter'
# print(line_1)
# print(line_2)
# print(line_3)
# print(line_4)
# print(r'''
#             \n - enter
#             \t - Tab''')

# flower = '''

#                                      :^^^^:.
#                                  :?PBBBGGBBBGY~
#                                :P&B?^.    .^7P&B!           .^~!!!~:.
#                               !@#~            :P@5       ^JG#BGPPPGBBP?.
#                              ^@#:       .       5@J    :P@G?^.     .^J#&Y.
#                              Y@?        7.      .#@^  ?@#~             ?@B:
#                              Y@J        .7.  .:  ?@5 5@5.       ..      !@G
#                     .^!^     :&&^        :7. :7  :&&B@?  ::   .~~        B@:
#          ~5GP?.    ~##P&B^    ~&&!   :.   ^!..7.  G@@7  :7. .~!:        .#@5J7~.
#         ~@#!J&#?...5@G!?B@?.   .P@Y. .!~.  ^~:!^  Y@7  :!..^~:          Y&#&&&##P7.
#         ~&@BB5J#BGGBBBBG!Y#BGGP5JB@#!  :~^::~^^^: JY  ^!^^~:   .:.    ~G@@@@@@@&#&#!
#       .P&PPGPP?JPP5~?P5P5YY7!JJJY5G#@G!  :!^ ^~:^^7^^:^:^~..:^~~:  :7G@@@@@@@@@@@&B@?
#       :&@?J#BG@@??5B@@@&BPY~!??7!~^:^7J7^ :::^^~!7?!~^~^ :!^:.  :7P&@@@@@@@@@@@@@@&B@^
#        :?55?. P&PG@@@P!.               .^~^^!7~7Y7?Y7~:~.^..:~7JGB##&@@@@@@@@@@@@@@B@5
#                ^!?&&7          :^^^^^^^^:^^!??JJ?JJJ77?!~~7??7~^5BBBBB#&@@@@@@@@@@@#B&:
#                  P@7       .....:::^^~7..!^~!7J?JP?JYJ?!~^^. .. .:^!7JY5G#@@@@@@@@@@G@7
#                 .&&.     .^^^^^::::...^^.::^!??JY?J??!~~^~ !~^^^^::.    .^?G@@@@@@@@B&B
#                  B@~              .:^^^::.:!~!7!?.???!^:^:.~~~^::...       .J&@@@@@@@G@7
#                  ~@#^           :~^:   :!YP~.^^^!::^^~:.:~~: .:^^^^:.        J@@@@@@@#B@!
#                   ~B&J:           .^7YGBBP: .!:::::^ ^~^  :~~.   .:^~~^.     :#&@@@@@@#B&J.
#                    ^P@&P?7!~~!?YPB&@@&#B?   ~^~!.^~: .^!G~  .~~.      ..     ^&&#&&&&&@&B&B?.
#                :!YG####&@@@@@@@@@@@&#BGJ.  !^ ~^  ~~  ~.P@B7.  .            .G@?:~7YPGB#&#B@#.
#            :!YG#&&&&@@@@@@@&&&###BBB#&G.  !^ .7.  :7  ~Y.B@@#P!.           !#@?       .^~7JY7
#         .JGB###&@@@@@@@@@@@@@@@@@@@@@&^   .  ^!    ~. .&J.YP5Y?GP?~^:::^7YB&5:
#         ~@&B###&&&&&&@@@@@@@@@@@@@@@@Y       7:       .#@J:#@BY##5GGBBBBPY!.
#          .^^^^^~7JPB#&#&@@@@@@@@@@@@@?      .7        :&&?Y~P@@GJ!!~...
#                    .^JG###&@@@@@@@@@@B.     ..        J@!?@#775PPPP&B^
#                        ^?G#&#&@@@@@@@@P:             J@@J5@#@P!Y#57B@~
#                           ^?P##&&&&&&&&&5~.      .^J#&J7YJ! ^G@5!P@@Y~:
#                              .~7?JJJ?7^~5B#GP55PGB#G?.       J@Y5GY5GG&P.
#                                           :~!777~^.         .#@^J@@&J!&@^
#                                                             .G@PP@5?PPY^
#                                                               ~?7^

# '''
# print(flower)


import re
digits = '12458756'
letters = 'jdhyfuoalskkjd'
line = 'Lorem ipsum dolor sit amet'
digLetter = 'adsfg4343536g'
word = 'Apple'
word2 = 'BANANA'

print("================== isalnum() =====================")
print('\t', digits, ' ----> ', digits.isalnum())
print('\t', letters, ' ----> ', letters.isalnum())
print('\t', line, ' ----> ', line.isalnum())
print('\t', digLetter, ' ----> ', digLetter.isalnum())
print('\t', word, ' ----> ', word.isalnum())
print('\t', word2, ' ----> ', word2.isalnum())
print('==================================================\n\n')

print("================== isalpha() =====================")
print('\t', digits, ' ----> ', digits.isalpha())
print('\t', letters, ' ----> ', letters.isalpha())
print('\t', line, ' ----> ', line.isalpha())
print('\t', digLetter, ' ----> ', digLetter.isalpha())
print('\t', word, ' ----> ', word.isalpha())
print('\t', word2, ' ----> ', word2.isalpha())
print('==================================================\n\n')


print("================== isdigit() =====================")
print('\t', digits, ' ----> ', digits.isdigit())
print('\t', letters, ' ----> ', letters.isdigit())
print('\t', line, ' ----> ', line.isdigit())
print('\t', digLetter, ' ----> ', digLetter.isdigit())
print('\t', word, ' ----> ', word.isdigit())
print('\t', word2, ' ----> ', word2.isdigit())
print('==================================================\n\n')


print("================== islower() =====================")
print('\t', digits, ' ----> ', digits.islower())
print('\t', letters, ' ----> ', letters.islower())
print('\t', line, ' ----> ', line.islower())
print('\t', digLetter, ' ----> ', digLetter.islower())
print('\t', word, ' ----> ', word.islower())
print('\t', word2, ' ----> ', word2.islower())
print('==================================================\n\n')


print("================== isupper() =====================")
print('\t', digits, ' ----> ', digits.isupper())
print('\t', letters, ' ----> ', letters.isupper())
print('\t', line, ' ----> ', line.isupper())
print('\t', digLetter, ' ----> ', digLetter.isupper())
print('\t', word, ' ----> ', word.isupper())
print('\t', word2, ' ----> ', word2.isupper())
print('==================================================\n\n')

word += " Fruit"
print("================== istitle() =====================")
print('\t', digits, ' ----> ', digits.istitle())
print('\t', letters, ' ----> ', letters.istitle())
print('\t', line, ' ----> ', line.istitle())
print('\t', digLetter, ' ----> ', digLetter.istitle())
print('\t', word, ' ----> ', word.istitle())
print('\t', word2, ' ----> ', word2.istitle())
print('==================================================\n\n')


print("================== isspace() =====================")
print('\t', digits, ' ----> ', digits.isspace())
print('\t', letters, ' ----> ', letters.isspace())
print('\t', line, ' ----> ', line.isspace())
print('\t', digLetter, ' ----> ', digLetter.isspace())
print('\t', word, ' ----> ', word.isspace())
print('\t', word2, ' ----> ', word2.isspace())
print('==================================================\n\n')


print("================== lower() =====================")
print('\t', digits, ' ----> ', digits.lower())
print('\t', letters, ' ----> ', letters.lower())
print('\t', line, ' ----> ', line.lower())
print('\t', digLetter, ' ----> ', digLetter.lower())
print('\t', word, ' ----> ', word.lower())
print('\t', word2, ' ----> ', word2.lower())
print('==================================================\n\n')


print("================== upper() =====================")
print('\t', digits, ' ----> ', digits.upper())
print('\t', letters, ' ----> ', letters.upper())
print('\t', line, ' ----> ', line.upper())
print('\t', digLetter, ' ----> ', digLetter.upper())
print('\t', word, ' ----> ', word.upper())
print('\t', word2, ' ----> ', word2.upper())
print('==================================================\n\n')

print("================== capitalize() =====================")
print('\t', digits, ' ----> ', digits.capitalize())
print('\t', letters, ' ----> ', letters.capitalize())
print('\t', line, ' ----> ', line.capitalize())
print('\t', digLetter, ' ----> ', digLetter.capitalize())
print('\t', word, ' ----> ', word.capitalize())
print('\t', word2, ' ----> ', word2.capitalize())
print('==================================================\n\n')


print("================== title() =====================")
print('\t', digits, ' ----> ', digits.title())
print('\t', letters, ' ----> ', letters.title())
print('\t', line, ' ----> ', line.title())
print('\t', digLetter, ' ----> ', digLetter.title())
print('\t', word, ' ----> ', word.title())
print('\t', word2, ' ----> ', word2.title())
print('==================================================\n\n')


print("================== swapcase() =====================")
print('\t', digits, ' ----> ', digits.swapcase())
print('\t', letters, ' ----> ', letters.swapcase())
print('\t', line, ' ----> ', line.swapcase())
print('\t', digLetter, ' ----> ', digLetter.swapcase())
print('\t', word, ' ----> ', word.swapcase())
print('\t', word2, ' ----> ', word2.swapcase())
print('==================================================\n\n')


line += " ipsum sit dolor ipsum"
print("================== find('substr') =====================")

# print('\n\t', line, ' ----> ', line.find('ipsum'), '\n')
# print('\n\t', line, ' ----> ', line.find('ipsum', 7), '\n')
# print('\n\t', line, ' ----> ', line.find('ipsum', 28), '\n')
# print('\n\t', line, ' ----> ', line.find('ipsum', 44), '\n')

index = -1
while True:
    index = line.find('ipsum', index + 1)
    print('\n\t', line, ' ----> ', index, '\n')
    if index == -1:
        break

print('==================================================\n\n')


print("================== rfind('substr') =====================")

print('\n\t', line, ' ----> ', line.rfind('ipsum'), '\n')

print('==================================================\n\n')


print("================== index('substr') =====================")

print('\n\t', line, ' ----> ', line.index('ipsum'), '\n')

print('==================================================\n\n')


print("================== rindex('substr') =====================")

print('\n\t', line, ' ----> ', line.rindex('ipsum'), '\n')

print('==================================================\n\n')


print("================== count('substr') =====================")

print('\n\t', line, ' ----> ', line.count('ipsum'), '\n')

print('==================================================\n\n')


numbersF = 4.23569

# print("text {3:2f}".format(numbersF))
numbers = '123'
line_1 = '234'
line_2 = 'Lorem 21 Hello'


print(re.search(r'1', numbers))
print(re.search(r'1', line_1))
print(re.search(r'1', line_2))

print()


print(numbers, " --> ", re.search(r'12', numbers))
print(line_1, " --> ", re.search(r'12', line_1))
print(line_2, " --> ", re.search(r'12', line_2))


print()
print(numbers, " --> ", re.search(r'[12]', numbers))
print(line_1, " --> ", re.search(r'[12]', line_1))
print(line_2, " --> ", re.search(r'[12]', line_2))


print()
print(numbers, " --> ", re.search(r'[0-4]', numbers))
print(line_1, " --> ", re.search(r'[4-9]', line_1))
print(line_2, " --> ", re.search(r'[0-9]', line_2))

match = re.search(r'[0-4]', numbers)
if match:
    print("Ok")
else:
    print('Not found')

print()

match = re.search(r'[5-9]', numbers)
if match:
    print("Ok")
else:
    print('Not found')


line_2 = '***Lorem 21 Hello'
print(line_2, " --> ", re.search(r'[^*]', line_2))
print(line_2, " --> ", re.findall(r'\w+', line_2))

match = re.search(r'[^*]', line_2)
print(match.group(0))


# print(line, " --> ", re.sub(r'[^m]{5}', 'blue', line))
# # print(line, '--->', line.replace('ipsum', 'test'))
