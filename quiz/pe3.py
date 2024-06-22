#H24126078鄭雅云

print("Welcome to the simple calculator program!")

ifContinue = True
#如果是True迴圈會繼續

while ifContinue == True:
	n1 = float(input("Enter the first number:"))
	n2 = float(input("Enter the second number:"))
	choose = str(input("Select an arithmetic operation(+,-,*,/):"))

	if choose == "+":
		print("Result:", float(n1 + n2))
	if choose == "-":
		print("Result:", float(n1 - n2))
	if choose == "*":
		print("Result:", float(n1 * n2))
	if choose == "/":
		if n2 == 0:
			print("Error: Division by zero!")
			continue   ###回到迴圈起點
		else:
			print("Result:", float(n1 / n2))


	continue_again = input("Do you want to perform another calculation?(yes or no):")\
	###再次選擇要不要繼續，如果yes，就是True，如果是no，那ifContinue會變成no，迴圈就不會再繼續了###

	if continue_again == "yes":
		ifContinue = True
	else :
		ifContinue = False
		print("Goodbye!")
