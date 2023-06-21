
start = 1
end = 10

if start > end:
    start,end = end,start

i = start
print("Task 1.3 --> \t ",end="")
while i <= end:
    if i % 7 == 0:
        print(i,end="\t")
    i+=1

print()

i = start
counter = 0
while i <= end:
    if i % 5 == 0:
        counter+=1
    i+=1
else:
    print("Task 1.4 --> \t ",counter)