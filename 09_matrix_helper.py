# import string

# letters = string.ascii_lowercase[0:8]
# number = string.digits[1:9]
# matrix = []
# for i in range(8):
#     matrix.append([' ' for i in range(8)])

# x = 4-1
# y = 3-1

# matrix[y][x] = 'T'



# i = y
# while i > 0:
#     i-=1
#     matrix[i][x] = '*' 
# for i in range(y+1,len(matrix)):
#     matrix[i][x] = '*' 

# for i in range(len(matrix[y])):
#     if matrix[y][i] != 'T':
#         matrix[y][i] = '*'

# for item in matrix:
#     print(item)

import random

matrix = []
row = 3
col = 4
for i in range(row):
    matrix.append([random.randrange(1,20) for j in range(col)])


for item in matrix:
    sum_ = 0
    for i in item:
        print(i,end='\t')
    print('| ',sum(item))
total_sum = 0
for i in range(col):
    print('-'*10,end='')
print()
for i in range(col):
    sum_ = 0
    for j in range(row):
        sum_ += matrix[j][i]
    print(sum_,end='\t')
    total_sum+=sum_
print('| ',total_sum)