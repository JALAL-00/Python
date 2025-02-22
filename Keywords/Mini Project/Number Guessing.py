import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("🎯 Welcome to the Number Guessing Game!")
print("You have 5 attempts to guess the secret number between 1 and 100.")
print("Type 'skip' to skip an attempt.")

# Using a for loop to limit attempts
for attempt in range(1, 6):  
    try:
        user_input = input(f"\nAttempt {attempt}/5: Enter your guess: ")

        if user_input.lower() == "skip":
            print("⏭️ Attempt skipped!")
            continue  # Skips the rest of this loop iteration and goes to the next attempt

        guess = int(user_input)  # Convert input to integer

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the correct number: {secret_number}")
            break  # Exits the loop immediately if guessed correctly
        elif guess < secret_number:
            print("📈 Too low! Try again.")
        else:
            print("📉 Too high! Try again.")

    except ValueError:
        print("⚠️ Invalid input! Please enter a number.")  
        pass  # Does nothing, allows the loop to continue

else:
    print(f"\n❌ Game Over! The secret number was: {secret_number}")
