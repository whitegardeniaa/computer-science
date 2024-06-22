#統計系116
#H24126078
#鄭雅云

v = input("Input velocity: ")
v = float(v)
#輸入速度，然後轉換為可以計算的小數

c = 299792458

p = v/c
print("Percentage of light speed=",p)
#輸出速度和光速的比率

gamma = 1/(1-(v**2/c**2))**(0.5)
#先算gamma的公式

td_alpha = float(4.3)
td_barnard = float(6.0)
td_betelgeuse = float(309)
td_andromeda = float(2000000)
#給定已知數據

tp_alpha = td_alpha/gamma
tp_barnard = td_barnard/gamma
tp_betelgeuse = td_betelgeuse/gamma
tp_andromeda = td_andromeda/gamma
#給定四個個別的公式

print("Travel time to Alpha Centauri=", tp_alpha)
print("Travel time to Barnard's Star=", tp_barnard)
print("Travel time to Betelgeuse (in the Milky Way) =", tp_betelgeuse)
print("Travel time to Andromeda Galaxy (closest galaxy)=", tp_andromeda)
#印出四個個別的結果
