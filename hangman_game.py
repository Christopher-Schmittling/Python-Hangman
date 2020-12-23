# Import Statements
import random
import hangman_art
import hangman_words

# Choose a random word from list
selected_word = hangman_words.word_list[random.randint(0,len(hangman_words.word_list) - 1)]

#Initial game setup
print(hangman_art.logo)
print("Welcome to Hangman!")

end_of_game = False
gallows = 6

#Hide the selected word
hidden_word = []

for letters in selected_word:
  hidden_word.append("_")

while not end_of_game:
  print(f"{' '.join(hidden_word)}")

  user_guess = input("Guess a letter: ")
  # Code for when you guess correct
  if user_guess in selected_word:
    for i in range(len(selected_word)):
      if user_guess == selected_word[i]:
        hidden_word[i] = user_guess
        # Check for end of game
        if "_" not in hidden_word:
          print("Congratulations, you won.")
          end_of_game = True
  # Code for when you guess incorrect
  else:
    gallows -= 1
    print(f"Sorry, {user_guess} in not in the word.")
    # Check for end of game
    if gallows == 0:
      print("You Lose")
      end_of_game = True

  print(hangman_art.stages[gallows])
