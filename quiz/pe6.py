#H24126078
#鄭雅云
#統計116


import random

answer = random.randint(97, 122) ##在97~122之間隨機生成一個數字，包含97和122

##ord("a") = 97, ord("z") = 122
##ord("A") = 65, ord("Z") = 90

history = [] ##蒐集所有猜測字母的
history_number = [] ##蒐集所有猜測字母的代表數字的
i = 0
while True:
	guess = input("Guess the lowercase alphabet: ")
	guess_number = ord(guess)
	if guess_number <= 97 and guess_number >= 122:
		print("Please enter a lowercase alphabet.")
		continue  ##直接再一次while迴圈

	if guess_number != answer:
		i += 1 ##這是猜測次數
		history.append(guess)
		history_number.append(guess_number)
		if guess_number > answer:
			print("The alphabet you are looking for is alphabetically lower.")
			continue
		if guess_number < answer:
			print("The alphabet you are looking for is alphabetically higher.")
			continue

	if guess_number == answer:
		print("Congratulations! You guessed the alphabet %s in , %d, tries." %(guess, i))
		break



print("Guess Histogram: ")
a_and_d = history_number.count(97) + history_number.count(98) + history_number.count(99) + history_number.count(100)
print("a - d: ", "*" * a_and_d)

e_and_h = history_number.count(101) + history_number.count(102) + history_number.count(103) + history_number.count(104)
print("e - h: ", "*" * e_and_h)

i_and_l = history_number.count(105) + history_number.count(106) + history_number.count(107) + history_number.count(108)
print("i - l: ", "*" * i_and_l)

m_and_p = history_number.count(109) + history_number.count(110) + history_number.count(111) + history_number.count(112)
print("m -p: ", "*" * m_and_p)

q_and_t = history_number.count(113) + history_number.count(114) + history_number.count(115) + history_number.count(116)
print("q - t: ", "*" * q_and_t)

u_and_x = history_number.count(117) + history_number.count(118) + history_number.count(119) + history_number.count(120)
print("u - x: ", "*" * u_and_x)

y_and_z = history_number.count(121) + history_number.count(122)
print("y - z: ", "*" * y_and_z)

##count就是屬串列中有幾個要找的目標值