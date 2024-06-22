#統計系116
#H24126078
#鄭雅云
n = int(input("Input the range number:"))

perfect_number=[]

for i in range(1,n):
    factor_sum = 0
    for j in range(1, int(i/2)+1):
        if i % j == 0:
            factor_sum = factor_sum + j

    if factor_sum == i:
        perfect_number.append(factor_sum)

print(perfect_number)
