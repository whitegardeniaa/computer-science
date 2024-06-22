###統計系116
###H24126078鄭雅云

import random

def safeorpenalty():
	board_with_penalty = []
	for _ in range(30):
		if random.random() < 0.3:
			board_with_penalty.append("P")
		else:
			board_with_penalty.append("_")

	return "".join(board_with_penalty)


board_with_penalty = safeorpenalty()  ##程式運行內部的遊戲板
updated_board = ["_" for i in range(30)]  ##玩家所見的遊戲板


def update(location_A, location_B):
    updated_board = ["_" for i in range(30)]

    if location_A == location_B:
        if board_with_penalty[location_A] == "P":
            updated_board[location_A] = "x"
        else:
            updated_board[location_A] = "X"
    else:
        if board_with_penalty[location_A] == "P":
            updated_board[location_A] = "a"
        else:
            updated_board[location_A] = "A"
        if board_with_penalty[location_B] == "P":
            updated_board[location_B] = "b"
        else:
            updated_board[location_B] = "B"

    return "".join(updated_board)


def game():
	location_A = 0
	location_B = 0
	penalty_A = 0
	penalty_B = 0

	while True:

		if penalty_A == 1:
			penalty_A -= 1
			step_A = 0
		else:
			step_A = random.randint(1, 6)
			location_A += step_A
			if location_A >= 30:
				location_A = 29
			if board_with_penalty[location_A] == "P":
				penalty_A = 1

		if penalty_B == 1:
			penalty_B -= 1
			step_B = 0
		else:
			step_B = random.randint(1, 6)
			location_B += step_B
			if location_B >= 30:
				location_B = 29
			if board_with_penalty[location_B] == "P":
				penalty_B = 1

		updated = update(location_A, location_B)

		print(updated, end="")
		print("(A: %d, B: %d)" %(step_A, step_B))

		if location_A == 29 and location_B == 29:
			print("Both players win!\n")
			print(board_with_penalty)
			break
		elif location_A == 29:
		    print('Player A wins!\n')
		    print(board_with_penalty)
		    break
		elif location_B == 29:
		    print('Player B wins!\n')
		    print(board_with_penalty)
		    break
		else:
		    continue

game()