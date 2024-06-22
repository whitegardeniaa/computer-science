##H24126078鄭雅云 統計116

sequence = input("Enter a sequence of integers separated by whitespace:")
sequence = sequence.split(" ")

new_sequence = []
for sequence in sequence :
	sequence = int(sequence)
	new_sequence.append(sequence)

new_sequence.sort(reverse = False)
print(new_sequence)

length = int(input("Length:"))

i = 0
while i < len(new_sequence)-1:
    if new_sequence[i] == new_sequence[i+1]:
        del new_sequence[i+1]
    else:
        i += 1

while len(new_sequence)> length:
	new_sequence.pop(-1)

print(new_sequence)