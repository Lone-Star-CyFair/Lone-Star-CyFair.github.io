import sys
import os
from random import randint

def clear():
  if sys.platform == "win32":
    os.system("cls")
  else:
    os.system("clear")

words = ["ant","baboon","badger","bat","bear","beaver","camel","cat","clam","cobra","cougar","coyote","crow","deer","dog",
"donkey","duck","eagle","ferret","fox","frog","goat","goose","hawk","lion","lizard","llama","mole","monkey","moose",
"mouse","mule","newt","otter","owl","panda","parrot","pigeon","python","rabbit","ram","rat","raven","rhino","salmon",
"seal","shark","sheep","skunk","sloth","snake","spider","stork","swan","tiger","toad","trout","turkey","turtle","weasel",
"whale","wolf","wombat","zebra"]

secret = words[randint(0, len(words) - 1)]

HANGMANPICS = ["""
  +---+
  |   |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

correct_letters = []
incorrect_letters = []

def prompt_user():
    # For now, take it for granted that "TEST".lower()
    # will return "test".
    letter = input("Enter your guess: ").lower()
    if len(letter) != 1:
        print("Your guess must only be one letter!")
        return prompt_user() # We prompt the user again
    elif letter < 'a' or letter > 'z':
        print("Your guess must be an English letter!")
        return prompt_user()
    return letter

def check_guess(letter):
    if letter in correct_letters or letter in incorrect_letters:
        # There's a better way of doing this, which
        # I'll introduce another time, but for now, None is not
        # a bad way to indicate that the letter's been guessed before.
        return None
    if letter in secret:
        correct_letters.append(letter)
        return True # Correct guess
    incorrect_letters.append(letter)
    return False # Incorrect guess

def unique_letters(word):
    unique = []
    for i in word:
        if not (i in unique):
            unique.append(i)
    return unique

def win_condition():
    if len(incorrect_letters) == len(HANGMANPICS) - 1:
        return False # User has lost
    if len(correct_letters) == len(unique_letters(secret)):
        return True # User has won
    return None # User has neither won or lost. Game is still going.


def win_screen():
    print(HANGMANPICS[len(incorrect_letters)])
    print("You won! The secret word was: " + secret)

def lose_screen():
    print(HANGMANPICS[-1])
    print("You lost! The secret word was: " + secret)

def print_incorrect_guesses():
    if incorrect_letters != []:
        print("Incorrect guesses: " + ", ".join(incorrect_letters))

def print_secret_word():
    print("Word: ", end="")
    for i in secret:
        if i in correct_letters:
            print(i, end=" ")
        else:
            print("_", end=" ")
    print()

def start_game():
    if win_condition() != None:
        if win_condition():
            win_screen()
            return
        else:
            lose_screen()
            return
    print(HANGMANPICS[len(incorrect_letters)])
    print_incorrect_guesses()
    print_secret_word()
    guess = prompt_user()
    clear()
    is_correct = check_guess(guess)
    if is_correct == None:
        print("You've already made the guess " + guess + "!")
    elif not is_correct:
        print(guess + " was incorrect!")
    else:
        print(guess + " was a good guess!")
    start_game()

clear()
start_game()
