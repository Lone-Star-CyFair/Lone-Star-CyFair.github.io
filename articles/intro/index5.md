![](cover.png)
<figcaption>Author: Amr Ojjeh</figcaption>
<figcaption>Cover By: Amr Ojjeh</figcaption>
<figcaption>Last updated: August 16, 2021</figcaption>

# Hangman

If you've not read the previous article, I encourage you to go [back](index4.html) and read it.

We'll now be writing hangman! When we're making a game, we have to ask, how do we represent our data?

(To see the full source code, visit [here](https://github.com/cyfaircs/cyfaircs.github.io/blob/main/articles/intro/hangman.py))

## Data

As we've mentioned before, we have all sorts of data types, but unfortunately, there's no "Hangman" type that's provided to us. As programmers, we have to compose the data types we have in order to be able to represent Hangman in memory. So, what kind of data does Hangman need?

Firstly, there's the secret word. That's the word which the user would have to guess.

	:::python
	secret = "elephant"
<figcaption>We'll discuss selecting new random words later.</figcaption>

We also want the hangman himself. Note though, that the hangman will have a different art depending on how many incorrect guesses the user took. As such, we can depict Hangman in all his stages by using a list:

	:::py
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
<figcaption markdown="span">You can see how the hangman looks on your terminal by printing him out with `print(HANGMANPICS[0])`</figcaption>

We also want to store the letters guessed correctly, and the letters guessed incorrectly.

	:::python
	correct_letters = []
	incorrect_letters = []
<figcaption markdown="span">The `[]` means it's an empty list. We'll be appending letters as the user guesses.</figcaption>

With that, we have all the data that we need! Notice how we can describe the state of the game with just these variables. This will make programming the game itself much easier.

Here's what the code should look like as of now:

	:::python
	secret = "elephant"

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


## The Game Loop

We're able to describe the game with data, but now we need to actually code the game. To do so, we need to think about how the game will work from the user's perspective. We can do this by writing what should the experience be when playing the game. Here's what I'm thinking:

	'e' was a good guess!
	  +---+
	  |   |
	  O   |
	 /|   |
	      |
	      |
	=========

	Incorrect guesses: z, x, y
	Word: e _ e _ _ _ _ _
	Enter your guess:


When the user enters their guess, the screen should clear, then print whether the guess was correct or incorrect, draw the new hangman picture, as well as the incorrect guesses and the word, and finally, it should once again prompt the user, unless there were too many incorrect guesses, or the word was guessed completely.

### Asking for Input

We as the programmer have a choice to pick any part of that cycle and start working on it. After we finish one part, we can add the next. Because I want to be able to test the game asap, I'll be working on the input functionality. Here's how we'd go about that:

	:::py
	def prompt_user():
		letter = input("Enter your guess: ")
		return letter

This code might look like it's enough, however, I ask you, what if the user enters a number? What if they enter multiple letters? What if they enter nothing at all? Those are cases we must handle if we wish our game to work consistently and without breaking. Here's how we do this:

	:::py
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

To keep this article short, I advise you to look at this code carefully and ask what the purpose of each line is.

### Checking correctness of input

Now that we have the input, we should check if it's correct or not. If it isn't, we add it to the incorrect list of letters. If it is, we can add it to the correct list.

	:::py
	def check_guess(letter):
		if letter in secret:
			# Just as lower, I insist that
			# you take .append for granted as well.
			# It simply means to add a single value to the list
			correct_letters.append(letter)
			return True
		else:
			incorrect_letters.append(letter)
			return False

Again, we must ask ourselves, is this enough? What if the user enters a letter they've already guessed before? Should we have duplicates in our list? As programmers, we must have an answer to these questions, otherwise, we do not know what our own program does. At its current state, lists can have duplicate letters, and users can correctly guess the same letter twice, as well as fail the same way twice. In my version of Hangman, I'd consider that impossible, so here's how I rectify the function:

	:::py
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
<figcaption markdown="span">Notice how we do not have an else anymore. This is because the `else` would be redundant, since if the prior `if` were to be true, the function would return True, and it would not proceed to complete the remainder of the code.</figcaption>

Note also that we did not print anything in the function `check_guess`. This is to keep most of the printing in one place, so that our code is organized.

### Win Condition

The game must eventually come to an end. This is done through a win, or a loss condition. Let's write a function which checks for that:

	:::py
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

I'll leave it as an exercise for you to understand the logic of these two functions.

### Writing the Main Loop

	:::py
	def start_game():
		print(HANGMANPICS[len(incorrect_letters)])
		guess = prompt_user()
		is_correct = check_guess(guess)
		if is_correct == None:
			print("You've already made the guess " + guess + "!")
		elif not is_correct:
			print(guess + " was incorrect!")
		else:
			print(guess + " was a good guess!")
		start_game()

We're almost there! We've defined all the functions that we need, so now we just need to call the `start_game` function to start our game. We can do this by calling the function at the end of the file, after all the functions have been defined. The hangman picture updates, the program is able to tell the difference between a good guess and a bad guess, but, we can't win or lose yet, and if we do lose, the program crashes. Also, it's the same secret word everytime, and the screen doesn't clear. Those are simple additions, however.

### Final Touches

Adding the win condition should be easy, as we've already defined the functions which we need for the logic to work. So, we just need to write two new functions that will print the lose or win screen, and write the logic in `start_game`:

	:::py
	def win_screen():
		print(HANGMANPICS[len(incorrect_letters)])
		print("You won! The secret word was: " + secret)

	def lose_screen():
		print(HANGMANPICS[-1])
		print("You lost! The secret word was: " + secret)

	def start_game():
		if win_condition() != None:
			if win_condition():
				win_screen()
				return
			else:
				lose_screen()
				return
		# ...

Selecting a random word requires us to *import* new functionality. I won't go too much about how this works, but you can write `from random import randint`. This will provide us with a function called `randint`, a function which we don't have to define, similar to how we don't have to define `print` or `input`.

We can now generate the secret word instead of assigning it `"elephant"`:
	
	:::py
	words = ["ant","baboon","badger","bat","bear","beaver","camel","cat","clam","cobra","cougar","coyote","crow","deer","dog",
	"donkey","duck","eagle","ferret","fox","frog","goat","goose","hawk","lion","lizard","llama","mole","monkey","moose",
	"mouse","mule","newt","otter","owl","panda","parrot","pigeon","python","rabbit","ram","rat","raven","rhino","salmon",
	"seal","shark","sheep","skunk","sloth","snake","spider","stork","swan","tiger","toad","trout","turkey","turtle","weasel",
	"whale","wolf","wombat","zebra"]
	secret = words[randint(0, len(words) - 1)]

`randint` will generate a random number between 0 and the length of the words list minus 1, and then use that number to select a random word from the words list.

Similarily, to clear the screen, we can `import os` and `import sys` at the top of the file, then define the function `clear` so that we can invoke it during our game loop:
	
	:::py hl_lines="10"
	def clear():
		if sys.platform == "win32":
			os.system("cls")
		else:
			os.system("clear")

	def start_game():
		# ...
		guess = prompt_user()
		clear()
		# ...

### Exercise
The game is completed! Mostly. If you look back at our vision, 

	'e' was a good guess!
	  +---+
	  |   |
	  O   |
	 /|   |
	      |
	      |
	=========

	Incorrect guesses: z, x, y
	Word: e _ e _ _ _ _ _
	Enter your guess:

you will see that we don't print the incorrect guesses, or the secret word as it's being filled. Writing those functions will be your exercise! The game loop should look like this after you're done:

	:::py hl_lines="10 11"
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

Good luck and have fun!