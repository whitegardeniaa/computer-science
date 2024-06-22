R = input("Please input a Richter scale value: ")
R = float(R)
#輸入Richter並轉為小數

print("Richter scale value: ", R )
#

ex = (1.5*R) + 4.8
Joules = 10**ex
#ex定義為指數，Joules為焦耳公式

print("Equivalence in Joules: ", Joules)
#輸出焦耳公式

TNT = Joules/(4.184*(10**9))
#根據倍數換算TNT
nutritious = Joules/2930200
#根據倍數換算營養午餐

print("Equivalence in tons of TNT: ", TNT)
print("Equivalence in the number of nutritious lunches: ", nutritious)
#輸出TNT和營養午餐



