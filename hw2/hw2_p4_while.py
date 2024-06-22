n = int(input("Enter the number of layers (2 to 5) ="))
a = int(input("Enter the side length of the top layer =")) 
d = int(input("Enter the growth of each layer ="))
w = int(input("Enter the trunk width (odd number, 3 to 9)="))
h = int(input("Enter the trunk height (4 to 10)="))

i = 1
while i <= n:
    if i == 1:
        j = 1
        while j <= a:
            if j == 1:
                print(((n-i)*d)*" " + (a-1)*" " + "#" + (a-1)*" ")
            elif 1 < j < a:
                print(((n-i)*d)*" " + (a-j)*" " + "#" + (2*(j-1)-1)*"@" + "#" + (a-j)*" ")
            elif j == a:
                print(((n-i)*d)*" " + (2*a-1)*"#")
            j += 1
    else:
        j = 2
        while j <= a+(i-1)*d+1:
            if j < (a+(i-1)*d):
                print(((n-i)*d)*" " + (i*d+a-d-j)*" " + "#" + (2*(j-1)-1)*"@" + "#" + (i*d+a-d-j)*" ")
            elif j == (a+(i-1)*d+1):
                print(((n-i)*d)*" " + (2*i*d+2*a-2*d-1)*"#")
            j += 1
    i += 1

i = 1
while i <= h:
    print(int(a+n*d-d-1-(0.5)*(w-1))*" " + w*"|")
    i += 1