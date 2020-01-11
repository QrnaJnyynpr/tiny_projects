import random

print("""
This program was designed to perform a basic test of
the 'random' method used in Python. It will perform
a coin toss repeated as many times as the user defines,
and then output the results.

The program will also track an aggregated result if
the test is repeated multiple times.

Note: the method Python uses to generate randomness
can only be considered \"pseudo-random\".

For more information, visit:
https://en.wikipedia.org/wiki/Pseudorandomness""")

heads_total = 0
tails_total = 0
repeat_total = 0

while True:
	repeat_count = int(input("\n| Please enter a repeat count:\n| "))
	repeat_total += repeat_count
	heads = 0
	tails = 0

	for i in range(1, repeat_count + 1):
		result = random.randint(0,1)

		if result == 0:
			heads += 1
			heads_total += 1
		else:
			tails += 1
			tails_total += 1

	print(f"""
| The psuedo-random module has generated:
|
| Heads: {heads}
| Tails: {tails}
|
| Instance repeat count:   {repeat_count}
| Aggregate repeat count:  {repeat_total}
| Aggregate Heads:         {heads_total}
| Aggregate Tails:         {tails_total}
""")