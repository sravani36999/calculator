import random  

secret_number = random.randint(1,100)

while True:
    guess_number = int(input("Enter a Guess Number: "))

    if guess_number > secret_number:
        print("Its too high.")
    elif guess_number < secret_number:
        print("Its too low.")
    else:
        print("Congratulations! You guessed correct number.")
        break 

#✏️ Your polished explanation:

'''I developed a small project called a Number Guessing Game using Python.
 In this project, I used a while loop and conditional statements.
  The computer generates a random number, and the user tries to guess it. 
  The program gives feedback like ‘too high’ or ‘too low’ until the correct number is guessed.
 This game helps children improve their memory and understand number comparison.'''