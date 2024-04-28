#Phillip John
#28 Apr 24
#P5HW
#A menu driven program that allows user to add or subtract random numbers.

import random

#Function to generate two random numbers
def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

#Function to add two generated numbers
def add_numbers():
    num1, num2 = generate_numbers()
    print(" ", num1)
    print("+", num2)
    return num1 + num2

#Function to subtract two generated numbers
def subtract_numbers():
    num1, num2 = generate_numbers()
    print("  ", num1)
    print("-", num2)
    return num1 - num2

#Function to handle adding operation
def handle_add():
    correct_answer = add_numbers()
    guess = None
    num_guesses = 0
    
    #Loop for guessing the sum
    while guess != correct_answer:
        guess = int(input("\nEnter answer: "))
        num_guesses += 1
        if guess < correct_answer:
            print("Sorry, guess is too low.")
        elif guess > correct_answer:
            print("Sorry, guess is too high.")
        else:
            print("Congratulations!!!! Your answer is correct.")
            print("Number of guesses:", num_guesses)
            break

#Function to handle subtracting operation
def handle_subtract():
    correct_answer = subtract_numbers()
    guess = None
    num_guesses = 0
    
    #Loop for guessing the difference
    while guess != correct_answer:
        guess = int(input("\nEnter answer: "))
        num_guesses += 1
        if guess != correct_answer:
            print("Sorry, that's not the correct answer. Try again.")
        else:
            print("Congratulations!!!! Your answer is correct.")
            print("Number of guesses:", num_guesses)
            break

#Main function
def main():
    print("Welcome to Math Quiz\n")
    menu_options = {
        1: handle_add,
        2: handle_subtract,
        3: exit
    }

    while True:
        print("\nMAIN MENU")
        print("-------------------------------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit\n")

        choice = int(input("Please choose one of the menu options: "))
        #Check if the choice is valid
        if choice in menu_options:
            if choice == 3:
                print("Thank you for playing....\nBye!!")
                break
            menu_options[choice]()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()



 
 



