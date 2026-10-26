# Number Guessing Loop 

secret = 7 
attempts = 0
guess = -1 

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print(f"Correct! You took {attempts} tries.")