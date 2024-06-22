n = int(input("Enter the size of the grid:"))
matrix = [["_" for i in range(n)]for j in range(n)]

for i in range(n):
	for j in range(n):
		print(matrix[i][j], end=" ")
	print()

while True:
	cell_coordinate = input("Enter the size of the grid: ")
	if cell_coordinate == "done":
		break
	new_value = input("Enter the new value for the cell: ")
	row, col = cell_coordinate.split(",")
	row, col = int(row), int(col)
	matrix[row][col] = new_value

	for i in range(n):
		for j in range(n):
			print(matrix[i][j], end=" ")
		print()