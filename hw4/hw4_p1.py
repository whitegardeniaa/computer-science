#H24126078鄭雅云
#統計116

import random

def grid():
	for i in range(0, 20):
		if i == 0 :
			print("     a   b   c   d   e   f   g   h   i")
		if i % 2 == 0 and i != 0:
			print(int(i/2), " |   |   |   |   |   |   |   |   |   |" )
		if i % 2 != 0 :
			print("   +---+---+---+---+---+---+---+---+---+")

###
#遊戲開始之前
###
grid()
print()
print("Enter the column followed by the row (ex: a5). \nTo add or remove a flag, add \'f\' to the cell (ex: a5f).\nType \'help\' to show this massage again.")
print()
inputt = str(input("Enter the cell (10 mines left):"))

def generate_random_mines(): ###生成隨機的地雷
	mines = set()
	while len(mines) < 10:
		row = random.randint(1, 9)
		col = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
		if (row, col) != (int(inputt[1]), inputt[0]):
			mines.add((row, col))
	return mines

# def grid_with_mines(mines): ###把地雷放進格線 print是在測試有沒有放進去 說實在的好像這定義沒什麼意義 最後也不會印出來
# 	print("    a   b   c   d   e   f   g   h   i")
# 	print("  +---+---+---+---+---+---+---+---+---+")
# 	for i in range(1, 10):
# 		row_str = str(i)
# 		row_str += " |"
# 		for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
# 			if (i, col) in mines:
# 				row_str += " X |"
# 			else:
# 				row_str += "   |"
# 		print(row_str)
# 		print("  +---+---+---+---+---+---+---+---+---+")

def count_the_mines(mines, row, col): ###數周圍地雷的數量
	number_of_mines_around = 0
	for r in range(row - 1, row + 2):
		for c in range(ord(col) - 1, ord(col) + 2):
			if (r, chr(c)) in mines:
				number_of_mines_around += 1
	return number_of_mines_around

def grid_with_number_of_mines_around(mines): ###把地雷的數量放進格線內
	print("    a   b   c   d   e   f   g   h   i")
	print("  +---+---+---+---+---+---+---+---+---+")
	for i in range(1, 10):
		row_str = str(i)
		row_str += " |"
		for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
			if (i, col) in mines:
				row_str += "   |"
			else:
				count = count_the_mines(mines, i, col)
				if count == 0:
					row_str += " 0 |"
				if count != 0:
					row_str += f" {count} |"
		print(row_str)
		print("  +---+---+---+---+---+---+---+---+---+")

def generate_board(rows, cols): ###生成遊戲板，初始時所有格子都是未揭開的
	board = [[' ' for _ in range(cols)] for _ in range(rows)]
	return board

def click_cell(board, mines, row, col): ###玩家點擊格子，打開相應的格子及其周圍的格子
	if board[row][col] != ' ':
		print("This cell has already been clicked!")
		return True
	else:
		open_neighbors(board, mines, row, col)
		grid_with_number_of_mines_around(mines)
		return True

def is_blank(board, row, col):
	return board[row][col] == ' '

def open_neighbors(board, mines, row, col): ###打開指定格子周圍一圈的格子
	offsets = [(-1, -1), (-1, 0), (-1, 1),
 				(0, -1),           (0, 1),
				(1, -1), (1, 0), (1, 1)]
    
	rows = len(board)
	cols = len(board[0])

	for dr, dc in offsets:
		r, c = row + dr, col + dc
		if 0 <= r < rows and 0 <= c < cols and is_blank(board, r, c):
			board[r][c] = str(count_the_mines(mines, r, c))
			if is_blank(board, r, c):
				open_neighbors(board, mines, r, c)

def put_flag(board, row, col):
	if board[row][col] == ' ':
		board[row][col] = 'F'
		print("Flag placed at", chr(col + ord('a')), row + 1)
	else:
		print("Cannot place flag here, cell already clicked or flagged!")

def main():
	board = generate_board(9, 9)
	mines = generate_random_mines()
	while True:
		grid_with_number_of_mines_around(mines)
		print()
		cell = input("Enter the column followed by the row (ex: a5) or add 'f' for flag: ")
		if cell[-1] == 'f':
			row = int(cell[1]) - 1
			col = ord(cell[0]) - ord('a')
			put_flag(board, row, col)
		else:
			row = int(cell[1]) - 1
			col = ord(cell[0]) - ord('a')
			click_cell(board, mines, row, col)

if __name__ == "__main__":
	main()