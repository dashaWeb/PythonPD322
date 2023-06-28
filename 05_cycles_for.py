

# line = "Hyper text markup language"

# print(line[1])

# for letter in line[0:20:2]:
#     print(letter, end=" ")


# for i in range(1,20,2):
#     print(i,end="\t")

# while True:
#     n = int(input("2 + 2 ? ->"))
#     if n == 4:
#         break
# print("Congratulation")

# i = 0
# n = int(input("Enter end number :: "))
# while i < n:
#     i+=1
#     if i % 3 == 0:
#         continue
#     print(i, end="\t")


#  31 11 7 5 13 17 19
# 6 8 12

# counter = 0
# number = int(input("enter number :: "))
# for i in range(1,number + 1):
#     if number % i == 0:
#         counter+=1

# if counter > 2:
#     print("prime")
# else:
#     print("simple")

# flag = True
# number = int(input("enter number :: "))
# for i in range(2,number//2 + 1):
#     if number % i == 0:
#         flag = False
#         break

# if not flag:
#     print("prime")
# else:
#     print("simple")

# number = int(input("enter number :: "))
# for i in range(2,number//2 + 1):
#     if number % i == 0:
#         print("prime")
#         break
# else:
#     print("simple")

import random
print("\t\tWelcome to the game")
print("\t\t Rock Paper Scissors")

user = 0
bot = 0

win_bot = 0
win_user = 0

while True:
    user_score = 0
    bot_score = 0
    for item in range(3):
        print("\n\n------------ Round # {} -------------".format(item + 1))
        while True:
            user = input(
                "\t [r] - rock; \n\t [p] - paper; \n\t [s] - scissors; \n\t Enter your choose :: ")
            user = user.lower()
            if user == 'r' or user == 'p' or user == 's':
                break
            else:
                print("Error. Enter true choose")
        bot = random.choice('rps')
        print("\t\t Bot \t User")
        print("\t\t [{}] \t [{}] ".format(bot, user))
        if user == 'r' and bot == 's' or user == 'p' and bot == 'r' or user == 's' and bot == 'p':
            user_score += 1
        elif bot == 'r' and user == 's' or bot == 'p' and user == 'r' or bot == 's' and user == 'p':
            bot_score += 1

    if user_score > bot_score:
        print("\n\t=============== Congratulation!!!! You won !!!! ======================")
        win_user += 1
    elif bot_score > user_score:
        print("\n\t================= Sorry!!!! You Loser !!!! =========================")
        win_bot += 1
    else:
        print("\n\t=================== Draw ==========================")

    while True:
        user = input("Play again? [y]- yes; [n] - no :: ")
        user = user.lower()
        if user == 'y' or user == 'n':
            break
        else:
            print("Error. Enter true choose")
    if user == 'n':
        break

print()
# Розширити гру -- Додати нові варіанти + спок, ящірка
# Збільшити кількість раундів до 5
# При виході з гри -- показати статистику ігор
# Bot win  :: 5
# User win :: 10
# Draw     :: 2
