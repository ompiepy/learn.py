# The Collatz Sequence

print('Enter your number:')

try:
	integer = int(input())
	def collatz(number):
		if number % 2 == 0:  # The number is even.
			return number // 2
		elif number % 2 != 0:  # The number is odd.
			return 3 * number + 1

	integer = collatz(integer)
	print(integer)

	while integer != 1:
		print(collatz(integer))
		integer = collatz(integer)
except ValueError:
	print('You must type an intger')

