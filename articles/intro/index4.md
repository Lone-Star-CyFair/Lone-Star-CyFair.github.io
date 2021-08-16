![](cover.png)
<figcaption>Author: Amr Ojjeh</figcaption>
<figcaption>Cover By: Amr Ojjeh</figcaption>
<figcaption>Last updated: June 6, 2021</figcaption>

# Loops and Functions

If you've not read the previous article, I encourage you to go [back](index3.html) and read it.

We're getting close! After this article, we'll be writing Hangman! But first, we must cover loops and functions.

## Loops

We've already covered lists in our previous [article](index3.html#lists). Specifically, we've covered: accessing an item in a list, finding the length of a list, adding to a list, and removing from a list. But we still don't know how we'd go about incrementing every value in a list. We could do something like this:

	:::python
	test = [1, 2, 3, 4]
	test[0] = test[0] + 1
	test[1] = test[0] + 1
	test[2] = test[0] + 1
	test[3] = test[0] + 1
	print(test) # [2, 3, 4, 5]

However, this would not be practical for any large list, and it would fail if the list were to change its size. So, as we've done in the past, we introduce a new feature: For Loops.

The concept is very simple. We need a way to go through every item in the list. Here's how we do that:

	:::python
	test = [12, 14, 11, 2, 4]
	for i in test:
		print(i)
	# Output:
	# 12
	# 14
	# 11
	# 2
	# 4

The `i` is variable with an arbitrary name, meaning we can give it any name:

	:::python
	test = [12, 14, 11, 2, 4]
	for hello in test:
		print(hello)
	# Same output as before

The variable `i` and `hello` are like any other variable, except Python will automatically change them value to be the next value in the list after the code within the for loop is run. That is how this for loop is able to print every value in the list on a separate line.

Notice though, that if we try to change the variable:

	:::python
	test = [12, 14, 11, 2, 4]
	for num in test:
		num = 1
	print(test) # [12, 14, 2, 4]

The value of the list does *not* change. That is because `num` is a copy of each item, and not the item itself. More can be written about this later, but for now, our problem remains, how do we change the value of each item?

We already know how to change the value of one item:

	:::python
	test = [12, 14, 11, 2, 4]
	test[0] = 4

And we know how to get the length of a list:

	:::python
	test = [12, 14, 11, 2, 4]
	len(test)

So, if we can loop through a list which simply increments from 0 to the specified length, then we can change every item. Fortunately, there's a `range` function which does exactly that.

	:::python
	test = [12, 14, 11, 2, 4]
	for i in range(len(test)):
		test[i] = 1
	print(test) # [1, 1, 1, 1, 1]

And if we want to increment every item then multiply it by two:

	:::python
	test = [12, 14, 11, 2, 4]
	for i in range(len(test)):
		test[i] += 1
		test[i] *= 2
		# += is just a short hand for test[i] = test[i] + 1
		# Similar shorthands exist, such as -=, *=, and /=, plus a few more.
	print(test) # [26, 30, 24, 6, 10]

## Functions

Functions are no new concept. We've been using them since the very beginning. `print`, `input`, `int`, `str`, `len`, `range` are all functions. For this section, we'll simply learn how to define our own.

To do this, we use the `def` keyword, followed by the name of the function, then the parameters, which could be empty, then the code itself. Here's an example:

	:::python
	def my_len(xs):
		counter = 0
		for i in xs:
			counter += 1
		return counter

This function, called `my_len`, takes a list, which it refers to as `xs`, and counts for every item in the list. Effectively, we've recreated the `len` function. To use this function:

	:::python
	def my_len(xs):
		counter = 0
		for i in xs:
			counter += 1
		return counter

	print(my_len([-2, 1, 2, 3, 4, "cool"])) # 6

Notice the new `return` keyword. It simply means that the function will be substituted with this return value, which in this is `counter`. So, the function call `my_len([-2, 1, 2, 3, 4, "cool"])`, is evaluated as `6`, and so the code is equivalent to `print(6)`.

[Earlier](index1.html#input), I've said that some functions don't return a "useful" value, such as `print`. Here's how we define a function that doesn't return a "useful" value:

	:::python
	def print_menu():
		print("Here are your options!")
		print("A. This is option A")
		print("B. This is option B")
		print("C. This is option C")
<figcaption markdown="span">Notice the empty paranthesis after `test`. This means the function takes no arguments.</figcaption>

As you can see, there is no explicit return value. However, by default, this function will return the special `None` value, as you can see:

	:::python
	val = print_menu()
	print(val) # None

The `None` value is of its own type, which carries no significant data. It's most often used as just a temporary placeholder for a variable, or in this case, for functions which do not return anything significant. There are more useful cases for it. For instance, a search function may return the first item which matches a criteria, or it may return None if no such item exists.

## Exercise
Write a function which given a word and a list of letters, it will return the subset of letters which are in the word.

When you're ready, you can read start reading the [next](index5.html) article.
