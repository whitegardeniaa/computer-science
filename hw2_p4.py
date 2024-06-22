#統計系116
#H24126078
#鄭雅云

n = int(input("Enter the number of layers (2 to 5) ="))
a = int(input("Enter the side length of the top layer =")) 
d = int(input("Enter the growth of each layer ="))
w = int(input("Enter the trunk width (odd number, 3 to 9)="))
h = int(input("Enter the trunk height (4 to 10)="))

#聖誕樹的樹葉

for i in range(1,n+1):
    if i == 1:
        for j in range(1, a+1):
            if j == 1:
                print(((n-i)*d)*" " + (a-1)*" " + "#" + (a-1)*" ")

            if j > 1 and j < a:
                print(((n-i)*d)*" " + (a-j)*" " + "#" + (2*(j-1)-1)*"@" + "#" + (a-j)*" ")

            if j == a:
                print(((n-i)*d)*" " + (2*a-1)*"#")

    else:
        for j in range(2,a+(i-1)*d+2):
            if j < (a+(i-1)*d):
                print(((n-i)*d)*" " + (i*d+a-d-j)*" " + "#" + (2*(j-1)-1)*"@" + "#" + (i*d+a-d-j)*" ")

            if j == (a+(i-1)*d+1):
                print(((n-i)*d)*" " + (2*i*d+2*a-2*d-1)*"#")

#聖誕樹的樹幹
for i in range(1,h+1):
    print(int(a+n*d-d-1-(0.5)*(w-1))*" " + w*"|")

    