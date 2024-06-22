#統計系116
#H24126078
#鄭雅云

F = input("Input the force:")
m1 = input("Input the mass of m1:")
r = input("Input the distance:")
#input數值

F = float(F)
m1 = float(m1)
r = float(r)
#把數值轉成小數，才可以計算

G=6.67*(10**-11)
r2 = r**2
#定義r2是r的平方

m2 = (F*r2)/(G*m1)
#這是計算m2的公式

print("The mass of m2 = ", m2)
#print出結果

c=299792458
E=m2*(c**2)
#這是計算能量的公式

print("The energy = ", E)
#print出結果