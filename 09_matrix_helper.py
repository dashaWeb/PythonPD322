import string

letters = string.ascii_lowercase[0:8]
number = string.digits[1:9]
matrix = []
for i in range(8):
    matrix.append([' ' for i in range(8)])

x = 4-1
y = 3-1

matrix[y][x] = 'T'



i = y
while i > 0:
    i-=1
    matrix[i][x] = '*' 
for i in range(y+1,len(matrix)):
    matrix[i][x] = '*' 

for i in range(len(matrix[y])):
    if matrix[y][i] != 'T':
        matrix[y][i] = '*'

for item in matrix:
    print(item)