![](cover.png)
<figcaption>Author: Amr Ojjeh</figcaption>
<figcaption>Cover By: Amr Ojjeh</figcaption>
<figcaption>Last updated: June 6, 2021</figcaption>

# Data Types

If you've not read the previous article, I encourage you to go [back](index2.html) and read it.

The goal of the series is to introduce the fundementals of programming, specifically in Python. We've covered if statements, and some basic input and output. However, there is one concept, the most important one, which I've avoided covering so far, and that is data types.

Recall in our last two articles, we used the functions `str` and `int`, but I've never really explained what either one does. Also recall the equality operators, such as `>=` and `==`, what do they return? And what's the difference between a string or a number? This article should answer all these questions.

I recommend you open your REPL alongside as you read this article, as you should execute any code shown here. A benefit of the repl is that you don't need to write `print` like I do in the code, as the REPL automatically prints the result (Read, Eval, **Print**, Loop).

## Types
Before we explore what each type is, it's important that we talk about what is a type, first, and why they even exist.

You may have heard before that computers run on numbers. Everything is either a 0 or a 1, or as they say, in binary. Yet, how come you don't see this text as a string of numbers, but as English?

This question may arise, because the statement above, while true, is incomplete. Not only everything in memory is stored in binary, a row of 0s and 1s, but the way the numbers are *interpreted,* can vary.

Suppose I give you a sticky note with the number 2 on it. This 2 on its own, means nothing. It *could* be denoting length, perhaps in meters, or it could be describing an area, maybe in ft<sup>2</sup>. However, until I specify what it represents, you are only left guessing.

Unlike a human, though, a computer cannot guess. It must be told what each number represents, and that is what types do. A type "integer," tells the computer that the number is a whole number. A type "float" indicates that the number has a fraction, such as 1.2. A "string," is a bit more complicated (think of how many languages there are!), but essentially, it tells the computer that these number**s** represent characters. How strings, floats, and integers differ will not be covered in this series, as that's a rabbit hole of its own, but if I ever write an article on this matter, I'll provide a link here.

There are a ton more types which exist in Python, but to keep this short, I'll be covering the most important ones.

## Numbers
As mentioned, there are two ways to represent numbers. They can either be an integer or float. An integer must be a whole number, while a float must have a fraction. You can observe the type of each variable or constant with the function `type`.

	:::py
	a = 2
	print(type(a)) # <class 'int'>
	b = 2.2
	print(type(b)) # <class 'float'>
<figcaption>The integer type is often obreviated as "int"</figcaption>

Each type comes with its own set of operations. The `+` sign, even though it's used with many different types, actually behaves differently depending on the types given. For now, the difference is minor, but you'll see a major difference when we get to [lists](#lists).

	:::python
	a = 2
	b = 2.2
	print(type(b + b)) # <class 'float'>
	print(type(a + a)) # <class 'int'>
	print(type(a + b)) # <class 'float'>
<figcaption class="span">The `+` operator returns different types depending on the operands. When it's given an integer and a float, it convers the integer to a float.</figcaption>

Subtraction and multipication behave similar to addition with respect to numbers, so they won't be covered.

Division, however, comes in two forms.

	:::python
	a = 4
	b = 3
	c = a / b
	d = a // b
	print(c) # 1.3333...
	print(type(c)) # <class 'float'>
	print(d) # 1
	print(type(d)) # <class 'int'>

A single slash, regardless of the operands, returns a float, while a double slash will truncate the fraction and return an int.

Note that you should be careful when comparing floats, as they are sometimes approximates. For instance:

	:::python
	print(.1 + .2) # 0.30000000000000004

This is due to the fact that numbers are stored in binary. This will be another topic for another time, however, as it goes beyond the scope of the series. If you require a workaround, message one of the officers. If you need an immediate solution, you can consult [Python's documentation](https://docs.python.org/3/library/math.html#math.isclose).

## Lists
In life, everyone would like their cookies under a single container, and that's what lists do. You can store a series of related, or unrelated (though that's not recommended), values as a single value.

	:::python
	words = ["lemon", "juice", "grape", "cow", "farm", "beer", "animal", 32]
	print(type(words)) # <class 'list'>
	print(words[0]) # lemon
	print(words[7]) # 32
	print(words[-1]) # 32
	print(words[-8]) # lemon
	print([1, 2, 3, 4][0]) # 1

We can use the index operator, `[]`, to reference an item in the list. The first item is referenced by 0. Referencing an item which doesn't exist, such as `words[8]` or `words[-9]`, returns an error and halts the program. Referencing a negative index refers from the end of the list.

We can also change a value using the index operator:

	:::python
	words = ["cat", "dog"]
	words[0] = "rat"
	print(words) # ['rat', 'dog']

Lists also utilize the `+` operation, but it has a different behavior. When two lists are added, they are appended.

	:::python
	some_numbers = [1, 2, 3, 4]
	other_numbers = [5]
	print(some_numbers + other_numbers + [1, 2, 3]) # [1, 2, 3, 4, 5, 1, 2, 3]

As with the `+`, lists also support multipication, `*`.

	::python
	print([2, 3] * 4) # [2, 3, 2, 3, 2, 3, 2, 3]

An error is returned when a list is added to any other type.

We can remove an item or items in a list using the `del` keyword:

	:::python
	test = [1, 2, 3, 4]
	del test[0]
	print(test) # [2, 3, 4]
	del test[1:3]
	print(test) # [2]

You can find the length of a list using the `len` function.

	:::python
	print(len([1, 2, 3, 4, 5])) # 5

Finally, we can retrieve a subset of the list using the colon, `:`, character:

	:::python
	print([1, 2, 3, 4, 5][1:3]) # [2, 3]
<figcaption>The "3" is exclusive. One way to think about it, is that 3 - 1 specifies the length of the list, starting from index 1.</figcaption>

## Strings
Strings are very similar to lists, except they are immutable, meaning they cannot be changed. And they are initialized by quotes (single or double) instead of brackets.

	:::python
	print(type("Hello!")) # <class 'str'>
	test = 'cool!'
	# test[0] = "d" # ERROR: NOT ALLOWED
	print(test[0]) # c
	print(test[1:3]) # oo
	print(test + "!") # cool!!
	print(test * 3) # cool!cool!cool!
	print(len(test)) # 5

## Booleans
Booleans can either be `True` or `False`. Operators which return booleans are all the comparison operators, such as `==`, `<=`, `>`, `>=`, `!=`, etc..

	:::python
	first = True
	print(type(first)) # <class 'bool'>
	print(first) # True
	print(first == True) # True
	print(first != True) # False
	print(3 > 2) # True
	print(3 > 3) # False
	print(3 >= 3) # True
<figcaption class="span">The `!=` means "not equal to."</figcaption>

Very importantly, if statements use booleans to judge whether they should run or not. You should also know that booleans have a lot of uniqeu operators, such as `not`, `and`, and `or`.

	:::python
	if True:
		print("This will print no matter what")
	if False:
		print("This will never print")

	if x > 2 and x < 4:
		print("We're in the range!")

The `and` operator means that both operands have to be `True` for `and` to also return `True`, otherwise it returns `False`.

The `or` operator means that only one of the operands have to be `True` for the expression to evaluate to `True`, otherwise it's `False`.

The `not` operator only takes one operand, and it always returns the opposite value. So, `not False` = `True`.

## Casting
Now we get to the functions `int`, `str`, `float`, and `list`. They should all make sense now. Say we have a string which we want to treat as an integer, how do we go about that? Assuming it's a valid string, i.e. there are no letters, we can use the `int` function to *cast* it.

	:::python
	test = "2"
	# print(test + 2) # error
	print(int(test) + 2) # 4

This is why we wrap our `input` with `int` when we're expecting an integer.

	:::python
	user_input = int(input("Enter your number: "))

If we would like a float instead of an int, we can use the `float` function. If you'd like to go from a number to a string, then you use the `str` function.

	:::python
	age = 24
	print("My age is " + str(24))

The `list` function is also important, but as its use cases have not become apparent yet, we will skip it for now.

## Exercise
Given the user's input, return half the string they entered. For instance, if the user enters "crazy", the program should print "cra". If they enter "lame", the program should print "la".

When you're ready, you can read start reading the [next](index4.html) article.
