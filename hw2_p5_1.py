#統計系116
#H24126078
#鄭雅云

n = int(input("Input an integer number:"))

def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 1:
        a, b = 0, 1
        for i in range (n-2):
            a, b = b, a+b
        return a+b

print("the", n, "-th Fibonacci sequence number is:", f(n))