import random

def get_random_word():
    word_list = ['Drink', 'Mouse', 'robot', 'Break', 'Brain','Crime','Catch']
    return random.choice(word_list)

def display_current_progress(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game():
    word = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("🔠 Let's play Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_attempts:
        print("\nWord:", display_current_progress(word, guessed_letters))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
            incorrect_guesses += 1

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You guessed the word:", word)
            break
    else:
        print(f"\n💥 You've run out of guesses. The word was: {word}")


hangman_game()
