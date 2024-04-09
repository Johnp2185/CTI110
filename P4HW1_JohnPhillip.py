#Phillip John
#6 Apr 24
#P4HW1
#A program that loops to collects the scores a user enters.

# Get the number of scores from the user
num_scores = int(input('How many scores do you want to enter? '))

# Print a blank line for readability
print()

# Initialize variables
scores = []
lowest_score = None
sum_scores = 0

# Loop to get scores from the user
i = 1  # Initialize score counter
while len(scores) < num_scores:  # Continue until all scores are obtained
    score_input = input(f'Enter score #{i}: ')
    score = float(score_input)
    if 0 <= score <= 100:
            # Update lowest score if it's None or the new score is lower
            if lowest_score is None or score < lowest_score:
                lowest_score = score
            scores.append(score)
            sum_scores += score
            i += 1  # Move to the next score
    else:
            print('\nINVALID Score entered!!!!\nScore should be between 0 and 100')
 
# Print a blank line for readability
print()

# Remove lowest score from the list
scores.remove(lowest_score)

# Calculate average score
average_score = sum_scores / num_scores

# Determine letter grade
if 90 <= average_score <= 100:
    letter_grade = 'A'
elif 80 <= average_score < 90:
    letter_grade = 'B'
elif 70 <= average_score < 80:
    letter_grade = 'C'
elif 60 <= average_score < 70:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Print the results
print('\n----------------Results-------------')
print(f'Lowest Score   : {lowest_score}')
print(f'Modified List  : {scores}')
print(f'Scores Average : {average_score:.2f}')
print(f'Grade          : {letter_grade}')
print('------------------------------------')
