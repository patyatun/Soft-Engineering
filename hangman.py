import random
import time

#Lists of words
colors = ["blue", "orange", "white", "brown", "purple", "yellow", "black", "gray", "pink", "red"]
animals = ["dog", "cat", "bear", "frog"]
fruits = ["apple", "banana", "lemon", "watermelon", "mango", "cherry", "strawberry", "grape"]

words = {"colors":colors[:], "animals":animals[:], "fruits":fruits[:]}

images = [
    '''
   +---+
       |
       |
       |
      ===
      ''', '''
   +---+
   O   |
       |
       |
      ===
      ''', '''
   +---+
   O   |
   |   |
       |
      ===
      ''', '''
   +---+
   O   |
  /|   |
       |
      ===
      ''', '''
   +---+
   O   |
  /|\  |
       |
      ===
      ''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===
      ''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===
      ''']


#Select a random word based on the player selection
def select_word():
    #The player enter the subject
    subject = input(f"Please enter the subject of the word {list(words.keys())}: ")
    return random.choice(words[subject])


#Show the actual state of the game
def visualize_hangman(wrong_letters, correct_letters, word):
    #Print the hangman image corresponding to the number of the wrong guesses
    print(images[len(wrong_letters)])
    print()

    #Print the wrong letters
    print("Wrong letters:", " ".join(wrong_letters))

    # Create a string of underscores representing unguessed letters
    blanks = "_" * len(word)

    # Replace underscores with correctly guessed letters in the word
    blanks = "".join([letter if letter in correct_letters else "_" for letter in word])

    # Display the target word with spaces between each letter or underscore for unguessed letters
    print("Correct letters:", " ".join(blanks))
    print()


#Get a valid letter guess from the user
#The user should only enter a single character and it must be a letter between a-z
def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        #Check if the input is a single character
        if len(guess) != 1:
            print("Please enter a single letter")
        #Check if the input is a letter that has already been guessed
        elif guess in guessed_letters:
            print("You had already entered that letter. Try again")
        #Check if the input is a letter between a-z
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter only letters (a-z)")
        else:
            return guess


#Function to ask the user if they want to play again      
def play_again():
    while True:
        response = input("Do you want to play again? Enter yes or no: ").lower()

        if response.startswith("y"):
            return True
        elif response.startswith("n"):
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


#Function to reset game variables
def reset_game():
    global wrong_letters, guessed_letters, target, finish_game
    wrong_letters = ""
    guessed_letters = ""
    finish_game = False
    target = select_word()


#Function to play
def hangman_game():
    global wrong_letters, guessed_letters, target, finish_game
    
    while True:
        visualize_hangman(wrong_letters, guessed_letters, target)

        # Let the player enter a letter
        guess = get_guess(wrong_letters + guessed_letters)
        
        if guess in target:
            guessed_letters += guess

            # Check if the player already guessed all the letters
            found_all_letters = all(letter in guessed_letters for letter in target)
            if found_all_letters:
                print(f"Congratulations! You guessed the word: {target}")
                finish_game = True
        else:
            wrong_letters += guess

            # Check if the player has guessed too many times and lost
            if len(wrong_letters) == len(images) - 1:
                visualize_hangman(wrong_letters, guessed_letters, target)
                print("Your attempts are over.")
                print(f"The word was {target}.")
                finish_game = True

        # Ask the player if they want to play again
        if finish_game:
            if play_again():
                reset_game()
            else:
                break


#Introduction for Hangman Game
#Name of the player
name = input("Welcome to the Hangman Game! What's your name? ")
wrong_letters = ""
guessed_letters = ""
#Select the subject of the word
target = select_word()
finish_game = False
print("Try to guess the word before the hangman is fully drawn")
print("You can guess one letter at a time. Good luck!\n")
print("Okay. Let's play")
time.sleep(1)

hangman_game()