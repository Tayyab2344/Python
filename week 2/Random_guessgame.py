import random

def start_game():
    print("Game is going to be start!!")
    print("Enter a number between 1-100")
    attempts = 0
    random_number = random.randint(1, 100)
    
    while True:
        guess = int(input("Enter your guess please: "))
        attempts += 1
        
        if guess > random_number:
            print("Too high!!")
        elif guess < random_number:
            print("Too low!!")
        else:
            print(f"Congratulations!! You guessed the number: {random_number} in {attempts} attempts.")
            break

start_game()
