import random
word_list = ["apple", "tiger", "chair", "robot", "house"]
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
guessed_letters = []
attempts = 6
print("🎮 Welcome to Hangman!")
print("Guess the word letter by letter.")
while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Attempts left:", attempts)
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    if guess in chosen_word:
        print("✅ Correct guess!")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1
if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)