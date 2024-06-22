#H24126078
#鄭雅云

money = int(input("Enter the shopping amount:"))
level = str(input("Enter the membership level (Regular of Gold):"))
#輸入價格和會員等級，格式為整數和字串

if level == "Regular":
	if money <=1000 :
		print("Regular", "$", money*1)
	elif 1000 < money < 2000 :
		print("Regular", "$", money*0.9)
	elif 2000 < money < 3000:
		print("Regular", "$", money*0.85)
	elif money > 3000:
		print("Regular", "$", money*0.8)
#會員等級為Regular
#底下再一個條件結構去輸入打折結果

elif level == "Gold":
	if money <=1000 :
		print("Gold", "$", money*1)
	elif 1000 < money < 2000 :
		print("Gold", "$", money*0.85)
	elif 2000 < money < 3000:
		print("Gold", "$", money*0.8)
	elif money > 3000:
		print("Gold", "$", money*0.75)
#會員等級為Gold
#底下再一個條件結構去輸入打折結果

else :
	print("Invalid membership level. Please enter 'Regular' or 'Gold'. ")
#在最外圈的，篩選會員等級的迴圈
#如果不是Regular和Gold
#就印出無效的字樣