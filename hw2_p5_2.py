#統計系116
#H24126078
#鄭雅云

string = str(input("Please enter a string:"))
n = len(string)

def palindromic(string):
    longest_palindromic = ""
    n = len(string)

    for center in range(n):
        left = center 
        right = center
        while left >= 0 and right < n and string[left] == string[right]:
            if (right - left + 1) > len(longest_palindromic):
                longest_palindromic = string[left:right+1]
            left = left - 1
            right = right + 1

    for center in range(n):
        left = center
        right = center + 1
        while left >= 0 and right < n and string[left] == string[right]:
            if (right - left + 1) > len(longest_palindromic):
                longest_palindromic = string[left:right+1]
            left = left - 1
            right = right + 1

    return longest_palindromic        

longest_palindromic = palindromic(string)
number = len(longest_palindromic)
print("Longest palindrome substring is:", longest_palindromic)
print("Lenghth is:", number)

