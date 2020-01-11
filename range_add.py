def rangeadd():
	total = 0
	
	print("\nEnter a range of numbers to find the total of all numbers added together\n")

	low = input("Enter lowest number:\n")
	high = input("\nEnter highest number:\n")

	low, high = int(low), (int(high)+1)

	for i in range(low, high):
		total += i
		print(f"+{i}: {total}")

	while True:
		repeat = input("\nGo again? y/n\n")
		if repeat == "y" or repeat == "yes":
			rangeadd()
		elif repeat == "n" or repeat == "no":
			return
		else:
			print("\nPlease enter a valid choice!")
		
rangeadd()