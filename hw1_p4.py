#統計系116
#H24126078
#鄭雅云

h = input("Input the height of the 1st ball:")
h = float(h)

m1 = input("Input the mass of the 1st ball:")
m1 = float(m1)

m2 = input("Input the mass of the 2nd ball:")
m2 = float(m2)
#輸入數值，並且轉換為可計算的小數

g = 9.8
v1_initial = (2*g*h)**(0.5)
v2_initial = 0
#定義初始速度，也就是Ball1從斜坡滑下來之後的速度
#計算公式是位能轉換成動能

print("The velocity of the 1st ball after slide:", v1_initial)
#印出球1的初始(從斜坡滑下來之後)速度

v2_final = ((2*m1)/(m1+m2))*v1_initial + ((m2-m1)/(m1+m2))*v2_initial
#彈性碰撞的公式，計算被碰撞物體的速度

print("The velocity of the 2nd ball after collision:", v2_final)
#印出球2碰撞後的速度