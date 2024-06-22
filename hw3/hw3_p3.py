#H24126078
#統計系
#鄭雅云

#定義二維空白的格子
rows = 6
columns = 7

board = []
i = 0 #i從row 0 開始
while i < rows:
	row = []
	j = 0 #j從column 0 開始
	while j < columns:
		row.append(" ")
		j += 1
	board.append(row)
	i += 1


#定義格線
line = "+---"*7 + "+"


#劃格線
i = 0
while i < rows : 
	print(line)
	j = 0
	while j < columns :
		print("| %s " %board[i][j], end="")
		j += 1
	print("|")
	i += 1
print(line)
print("  0   1   2   3   4   5   6")


#定義遊戲結束
def gameover(board):
	i, j = 0, 0
	while i < rows:
		j = 0
		while j < columns:
			if board[i][j] == " ":
				j += 1
				continue
			if j <= 3 and board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]:
				board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j].lower()
				return True, board[i][j]
			if i <= 2 and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]:
				board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i][j].lower()
				return True, board[i][j]			
			if i >= 3 and j <= 3 and board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3]:
				board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == board[i][j].lower()
				return True, board[i][j]
			if i <= 2 and j <= 3 and board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
				board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i][j].lower()
				return True, board[i][j]
			j += 1
		i += 1
	return False, ""

	i = 0
	while i < rows:
		j = 0
		while j < columns:
			if board[i][j] == " ":
				return False, None
			j += 1
		i += 1
	return True, "Draw"	

#定義合法放入棋子
def put(player):
	while True:
		try:
			col = int(input("Player %s, enter a column number (0-6):" %player))
			if col > 6 or col < 0:
				print("Out of range, try again [0-6].")
				continue
			if board[0][col] != " ":
				print("This column is full. Try another column.")
				continue
			return col
		except ValueError:
			print("Invalid input, try again [0-6].")

player1 = "O"
player2 = "X"
#定義完畢開始主程式
now_player = player1
while True:
	print("Player %s >>" % now_player)
	col = put(now_player)

	i = 5
	while i >= 0 :
		if board[i][col] == " ":
			board[i][col] = now_player
			break
		i = i - 1

	#畫新格子
	line = "+---"*7 + "+"
	i = 0
	while i < rows : 
		print(line)
		j = 0
		while j < columns :
			print("| %s " %board[i][j], end = "")
			j += 1
		print("|")
		i += 1
	print(line)
	print("  0   1   2   3   4   5   6")

    #遊戲結束
	over, winner = gameover(board)
	if over:
		if winner == "Draw":
			print("Draw")
		else:
			line = "+---" * 7 + "+"
			i = 0
			while i < rows:
				print(line)
				j = 0
				while j < columns:
					print("| %s " % (board[i][j]), end="")
					j += 1
				print("|")
				i += 1
			print(line)
			print("  0   1   2   3   4   5   6")
			print("Winner: %s" % winner)
		break

	#切換玩家
	if now_player == player1:
		now_player = player2
	else:
		now_player = player1