![](cover.png)
<figcaption>Author: Amr Ojjeh</figcaption>
<figcaption>Cover By: Amr Ojjeh</figcaption>
<figcaption>Last updated: June 6, 2021</figcaption>

# Intro to Python
If you've not read the previous article, I encourage you to go [back](index.html) and read it.

This is the first of many articles. The goal of these articles is to introduce you to Python quick and easy, and by the end of these articles, you should have written your first game, Hangman! But first, we must cover the basics.

## Installation
Installing Python is relatively simple. Head to the website at [python.org](https://www.python.org/), and go through the installation process.

Using Python should be just as easy. If you're on Windows, you can open `cmd`, otherwise, you can open the `terminal`. Type `py` or `python`, then press enter. You should be prompted with something like:

	:::
	Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:37:30) [MSC v.1927 32 bit (Intel)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>>

If you were not prompted with this, then please contact one of our officers, and we'll be ready to help. If you also don't wish to install Python, then feel free to use [repl.it](https://repl.it).

## Hello World
What you just opened is what's called the "REPL." That is, "Read, Eval, Print, Loop." Simply, it means that Python will read your input, evaluate it, print the result, and then keep repating that process until you quit the program.

Let's print something in the REPL! If you don't already have it open, just as before, you can open it by either typing `py` or `python` in the terminal.

	:::python
	>>> print("Hello World!")
	Hello World!
	>>>

What we just did, is we invoked the `print` function, which simply prints the characters we give it. Like a regular math function, we use paranthesis to denote what we're passing to the function. Think of `f(x) = 2x`. To evaluate the function where `x = 2`, we write: `f(2)`. Similiarily, `print` is a function which requires a paramater similar to `x`, and we pass it the value we want the function to print.

The value, `Hello World!`, is in quotes because it's what we call a `string`. It has that name because it could be thought of as a string of characters, and the reason why strings require quotes is simply to let the program know that we're not writing code, and as such, whatever is inside the string is arbitrary. For instance, we could've also written:

	:::python
	>>> print("gasjgaklsjg")
	gasjgaklsjg
	>>>

And it would work the same way.

## How are you?
By introducing two features, we can write a program which greets the user after they input their name.

### Input
To do this, as the program implies, we must take input. This can be done easily:

	:::python
	>>> input("Enter your name: ")
	Enter your name: Amr
	'Amr'
	>>>

There are two interesting behaviors to note. For one, the program pauses until I enter some text and hit enter. Secondly, after I do that, `'Amr'` is printed, even though we never used the `print` function.

The program pauses because that is what `input` does, it takes input, and it'll wait until it has the user's input. `'Amr'` is printed because, unlike `print`, `input` *returns* a value. This means that the `input` function is substituted with the user's input. Recall the math analogy, where `f(x) = 2x`. If we invoke `f(x)` as `f(2)`, then that value *can* be substited with its evaluation, `2(2)`, or just `4`. Where the analogy falls apart, is that functions don't always need to return a useful value. Also, function *must* be substitued by the value returned. In this case, `'Amr'` is the returned value. Note the single quotes, they are equivalent to double quotes, which indicate that the value is a `string`.

### Variables
We have a way to retrieve the input, but to reference it, we must store it. Doing this is also simple:

	:::python
	>>> name = input("Enter your name: ")
	Enter your name: Amr
	>>> name
	'Amr'
	>>>

`name` could've been anything. We could've called the variable `boogalo`, but `name` is the most appropriate. Notice, that `'Amr'` is no longer printed after we run `input`. This is because the result is stored in `name`, and the assignment operator, `=`, does not return any value, it only assigns a value.

We can reference the name stored by simply typing the variable name, as seen above. And we can intuitively use the `+` sign to add to the string, called concatinating. This, however, does not change `name`. To change it, we must use the assignment operator, `=`, again. 

	:::python
	>>> name + "!"
	'Amr!'
	>>> name
	'Amr'

### Completing the Program
Now we should be able to greet the user!

	:::python
	>>> name = input("Enter your name: ")
	Enter your name: Amr
	>>> print("Hello " + name + "!")
	Hello Amr!
	>>>

There's an obvious catch with the REPL. To run out program, we must supply it the code as we carry out the program. This does not make for a great user experience, and that is one of the reasons why we use scripts. All a script is, is the code we just wrote, but instead of constantly writing it, we can save it in a file that ends with `.py`.

So, using notepad, or whatever editor you prefer to use, you can write and save the following code as `greetings.py`, or whichever name you prefer to give your file.

	:::python
	name = input("Enter your name: ")
	print("Hello " + name + "!")

You may run the program now by either running `py greetings.py` or `python greetings.py` in your terminal. Note, that the terminal's current directory must be the same one the location of the file. You can change your directory with the command `cd`. Also note that the terminal is unrelated to Python, and is simply how we run Python.

From now on, all examples will be shown as if they were written and saved in a file. You are still encouraged, however, to the use the REPL for whenever you are experimenting, since you can run any python code without the hassle of saving.

## Exercise
Write a program which asks the user for their age, and print how old they would be in 10 years. To do this, you must use the `int` and `str` functions as such: 

	:::python
	some_number = int(input("Enter some number: ")) # Converts the string to an integer
	print("Is this your number? " + str(some_number)) # Convers the integer to a string
<figcaption markdown="span">More on these two functions will be written about [later](index3.html)</figcaption>

(Feel free to Google or ask for help! Always expect more examples in the upcoming articles, in the case you don't fully get something.)

When you're ready, you can read start reading the [next](index2.html) article.
