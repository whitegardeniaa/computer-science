#H24126078
#統計系
#鄭雅云

polynomial = input("Input polynomial:")
polynomial = polynomial.replace("+", " +").replace("-", " -")
polynomial = polynomial.split(" ")

x = float(input("Input the value of X: "))

value = 0
constant = 0
value_with_x = 0

i = 0
while i < len(polynomial):
    term = polynomial[i]
    if "^" in term:
        term = term.split("^")
        coefficient = term[0].split("X")
        value += float(coefficient[0]) * (x ** float(term[1]))
    elif not "X" in term:
        if "+" in term:
            constant += float(term.split("+")[1])
        elif "-" in term:
            constant -= float(term.split("-")[1])
    else:
        coefficient = term.split("X")
        value_with_x += float(coefficient[0]) * x

    i += 1

final_value = value + constant + value_with_x
print("Final value:", final_value)