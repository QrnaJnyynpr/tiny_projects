letter_bank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
	def rotate(user_entry, key):
		output = []
		for character in user_entry:
			if character not in letter_bank:
				output += character
			else:
				index = letter_bank.index(character)
				index += key
				if index > 25:
					index -= 26
				output += letter_bank[index]
		return output

	user_entry = input("\nEnter the text you wish to rotate:\n").lower()
	key = int(input("\nEnter a rotation key between 1-25:\n"))

	result = rotate(user_entry, key)

	print("\nYour rotated text is:")
	print("".join(result))