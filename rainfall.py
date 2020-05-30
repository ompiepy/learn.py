# Program corresponding to flowchart in this site https://automatetheboringstuff.com/2e/images/000039.jpg
print('Is raining? (Y)es or (N)o')
answer = input()
if answer == 'N':
	print('Go outside.')
elif answer == 'Y':
	print('Have umbrella? (Y)es or (N)o')
	answer2 = input()
	if answer2 == 'Y':
		print('Go outside.')
	elif answer2 == 'N':
		print('Wait a while.')
		print('Is raining? (Y)es or (N)o')
		answer3 = input()
		while answer3 == 'Y':
			print('Wait a while.')
			print('Is raining? (Y)es or (N)o')
			answer3 = input()
		print('Go outside.')
else:
	print("I can't understand you.Type 'Y' for yes and 'N' or No.")
print('===============')
print('Exiting program')

	


