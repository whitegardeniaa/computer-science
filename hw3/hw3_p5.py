#H24126078
#統計系
#鄭雅云

heights = input("Input sequence of seats: ")
heights = list(map(int, heights.split()))

n = len(heights)

left_max = [0] * n
right_max = [0] * n
##這是建立一個長度跟使用者輸入的長度一樣個串列

left_max[0] = heights[0]
for i in range(1, n):
    left_max[i] = max(left_max[i - 1], heights[i])


right_max[n - 1] = heights[n - 1]
for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], heights[i])
##for迴圈範圍的第三個-1，是因為想要從最右邊數回來


water_units = 0
for i in range(n):
    water_units += max(min(left_max[i], right_max[i]) - heights[i], 0)
##這個max(__, 0)，是因為如果有負數，可以確保負數不會被計算到


print("Water:", water_units)