#統計系116
#H24126078
#鄭雅云

n = int(input("The number ofthe requested element in Fibonacci (n) ="))
s1 = str(input("The first string for Palindromic detection (s1) ="))
s2 = str(input("The second string for Palindromic detection (s2) ="))
original = str(input("The plaintext to be encrypted:"))

print("----- extract key for encypt method -----")

#########Fibonacci Sequence#########
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

#########Fibonacci Sequence#########



#########Longest Palindromic substring(s1)#########
n1 = len(s1)

def palindromic(s1):
    longest_palindromic_s1 = ""
    n1 = len(s1)

    for center in range(n1):
        left = center 
        right = center
        while left >= 0 and right < n1 and s1[left] == s1[right]:
            if (right - left + 1) > len(longest_palindromic_s1):
                longest_palindromic_s1 = s1[left:right+1]
            left = left - 1
            right = right + 1

    for center in range(n1):
        left = center
        right = center + 1
        while left >= 0 and right < n1 and s1[left] == s1[right]:
            if (right - left + 1) > len(longest_palindromic_s1):
                longest_palindromic_s1 = s1[left:right+1]
            left = left - 1
            right = right + 1

    return longest_palindromic_s1        

longest_palindromic_s1 = palindromic(s1)
number = len(longest_palindromic_s1)
print("Longest palindrome substring is:", longest_palindromic_s1)
print("Lenghth is:", number)

#########Longest Palindromic substring(s1)#########



#########Longest Palindromic substring(s2)#########
n2 = len(s2)

def palindromic(s2):
    longest_palindromic_s2 = ""
    n2 = len(s2)

    for center in range(n2):
        left = center 
        right = center
        while left >= 0 and right < n2 and s2[left] == s2[right]:
            if (right - left + 1) > len(longest_palindromic_s2):
                longest_palindromic_s2 = s2[left:right+1]
            left = left - 1
            right = right + 1

    for center in range(n2):
        left = center
        right = center + 1
        while left >= 0 and right < n2 and s2[left] == s2[right]:
            if (right - left + 1) > len(longest_palindromic_s2):
                longest_palindromic_s2 = s2[left:right+1]
            left = left - 1
            right = right + 1

    return longest_palindromic_s2        

longest_palindromic_s2 = palindromic(s2)
number2 = len(longest_palindromic_s2)
print("Longest palindrome substring is:", longest_palindromic_s2)
print("Lenghth is:", number2)

#########Longest Palindromic substring(s2)#########



#########encrypted text#########

print("----- encryption completed -----")
name = "00000000000000000000000000000000000000000000000000000000000000000ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k = int(f(n))
a = int(number)
b = int(number2)
n3 = len(original)

changed = ""

for i in range(n3):
	x = name.find(original[i])
	y = x + k
	y2 = a*y + b
	if y2 > 90 :
		y3 = ((y2-65)%26)+65
	else:
		y3 = y2
	changed = changed + name[y3]

print("The encrypted text is: ", changed)