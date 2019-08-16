# This program tells you your letter grade based on numerical score input.
# It also checks whether the scores typed in were greater than 100 or less than 0
# Lastly, this program uses two while Loop to check if you are done.

# Give the program a title
print("      Welcome to Gilles Djomani's Grade Evaluator")
print("")
# Define 'done' to be the end of the loop
done = False
# While done is false
while not done:
        # Define each letter grade minimun score value
	A_score = 90
	B_score = 80
	C_score = 70
	D_score = 60
	# Ask for the test score
	score = int(input('Enter your test score: '))
	# Create a loop that checks if the score inputed is greater than 100 or less than 0
	while score < 0 or score > 100:
		print('Your score must be >= 0 and <= 100.  Please re-enter your test score: ')
		score = int(input('Enter your test score: '))
	# Display the letter grade according to the test score
	if score >= A_score:
		print('Your grade is A.')
	elif score >= B_score:
		print('Your grade is B.')
	elif score >= C_score:
		print('Your grade is C.')
	elif score >= D_score:	
		print('Your grade is D.')
	else:
		print('Your grade is F.')
	# Create a if command that checks whether to repeat the program
	another = input('Do you want to enter another quiz score? (y/n): ')
	if another == 'y' or another == 'Y':
		done = False
	else:
		done = True
exit = input('')
