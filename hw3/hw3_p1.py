#H24126078
#統計系
#鄭雅云

n = int(input("Input the total number of students (n>0):"))
number = list(range(1, n + 1))

index = 0

while len(number) > 1:
    i = 0
    while i < 3:
        if i == 2:
            number.pop(index)
            index = index - 1
        index = (index + 1) % len(number)
        i += 1

print("The last remaining number is:", number[0])
