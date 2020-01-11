import random

print("""
:::::::::::::::::::::::::::::::::::::::
Welcome to the random number generator!
:::::::::::::::::::::::::::::::::::::::
""")

while True:
	print("Enter your lowest possible whole number:")
	lowest = int(input())
	print("\nEnter your highest possible whole number:")
	highest = int(input())

	output = str(random.randint(lowest, highest))

	print(f"\nYour random number is:\n[ {output} ]\n")
	print(":::::::::::::::::::::::::::::::::::::::")