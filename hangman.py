import random

# Hangman stages
STAGES = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

words = ["python", "developer", "hangman", "challenge", "programming"]
word = random.choice(words)

display = ["_"] * len(word)
guessed_letters = []

wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman!")

while wrong_guesses < max_wrong:
    print(STAGES[wrong_guesses])   # 👈 show drawing
    print("Word:", " ".join(display))

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print("❌ Wrong!")
        print("Remaining chances:", max_wrong - wrong_guesses)

    if "_" not in display:
        print("🎉 You WON!")
        break

# Final result
if wrong_guesses == max_wrong:
    print(STAGES[wrong_guesses])
    print("💀 You LOST!")
    print("The word was:", word)