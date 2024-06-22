#H24126078
#統計系
#鄭雅云

xyk = input("Enter index x, y, k (separated by whitespace):")
xyk = xyk.split(" ")
x = int(xyk[0])
y = int(xyk[1])
k = xyk[2]
print("Enter the matrix by multiple lines:")

matrix = []
while True:
	without_process = input()
	if without_process == "q":
		break
	else :
		process = without_process.split(" ")
		matrix.append(process)

original = matrix[x][y]  ##定位使用者指定的位置
should_be_change = [(x,y)]  ##建立一個需要被更改的列表
while should_be_change:
	i, j = should_be_change.pop(0)
	if matrix[i][j] == original:
		matrix[i][j] = str(k)  ##先改掉使用者輸入的那個位置
		if i > 0 and matrix[i-1][j] == original :
			should_be_change.append((i-1,j))  ##左邊
		if i < len(matrix) - 1 and matrix[i+1][j] == original :
			should_be_change.append((i+1,j))  ##右邊
		if j > 0 and matrix[i][j-1] == original :
			should_be_change.append((i,j-1))  ##上面
		if j < len(matrix) - 1 and matrix[i][j+1] == original :
			should_be_change.append((i,j+1))  ##下面

i = 0
while i < len(matrix):
	j = 0
	while j < len(matrix[i]):
		print(matrix[i][j], end=" ") ##以空格間隔
		j += 1
	print() ##換行
	i += 1