In this chapter: We’ve added a variable named message. Every variable holds a value, which 
is the information associated with that variable. In this case the value is the 
text “Hello Python world!” 
Adding a variable makes a little more work for the Python interpreter. 
When it processes the first line, it associates the text “Hello Python world!” 
with the variable message. When it reaches the second line, it prints the value 
associated with message to the screen

Naming and Using Variables
When you’re using variables in Python, you need to adhere to a few rules 
and guidelines. Breaking some of these rules will cause errors; other guidelines just help you write code that’s easier to read and understand. Be sure 
to keep the following variable rules in mind:
•	 Variable names can contain only letters, numbers, and underscores. 
They can start with a letter or an underscore, but not with a number. 
For instance, you can call a variable message_1 but not 1_message.
•	 Spaces are not allowed in variable names, but underscores can be used 
to separate words in variable names. For example, greeting_message works, 
but greeting message will cause errors.
•	 Avoid using Python keywords and function names as variable names; 
that is, do not use words that Python has reserved for a particular programmatic purpose, such as the word print. (See “Python Keywords 
and Built-in Functions” on page 489.)
•	 Variable names should be short but descriptive. For example, name is 
better than n, student_name is better than s_n, and name_length is better 
than length_of_persons_name.
•	 Be careful when using the lowercase letter l and the uppercase letter O
because they could be confused with the numbers 1 and 0.
It can take some practice to learn how to create good variable names, 
especially as your programs become more interesting and complicated. As 
you write more programs and start to read through other people’s code, 
you’ll get better at coming up with meaningful names.

Strings
A string is simply a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around 
your strings like this: 
"This is a string."
'This is also a string.'
This flexibility allows you to use quotes and apostrophes within your 
strings:
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
Explore how to use strings in the file: string.py

Integers
Numbers are used quite often in programming to keep score in games, represent data in visualizations, store information in web applications, and so 
on. Python treats numbers in several different ways, depending on how they 
are being used. Let’s first look at how Python manages integers, because 
they are the simplest to work with.
You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.
n a terminal session, Python simply returns the result of the operation. 
Python uses two multiplication symbols to represent exponents(**)
Python supports the order of operations too, so you can use multiple 
operations in one expression. You can also use parentheses to modify the 
order of operations so Python can evaluate your expression in the order 
you specify.
Check int.py for practice on integers

Floats
Python calls any number with a decimal point a float. This term is used in 
most programming languages, and it refers to the fact that a decimal point 
can appear at any position in a number. Every programming language must 
Variables and Simple Data Types 31
be carefully designed to properly manage decimal numbers so numbers 
behave appropriately no matter where the decimal point appears.
For the most part, you can use decimals without worrying about how 
they behave. Simply enter the numbers you want to use, and Python will 
most likely do what you expect

Comments
Comments are an extremely useful feature in most programming languages. 
Everything you’ve written in your programs so far is Python code. As your 
programs become longer and more complicated, you should add notes within 
your programs that describe your overall approach to the problem you’re 
solving. A comment allows you to write notes in English within your programs.
How Do You Write Comments?
In Python, the hash mark (#) indicates a comment. Anything following a 
hash mark in your code is ignored by the Python interpreter
The main reason to write comments is to explain what your code is supposed to do and how you are making it work.


The Zen of Python
The Zen of Python
For a long time, the programming language Perl was the mainstay of the 
Internet. Most interactive websites in the early days were powered by Perl 
scripts. The Perl community’s motto at the time was, “There’s more than 
one way to do it.” People liked this mind-set for a while, because the flexibility written into the language made it possible to solve most problems 
in a variety of ways. This approach was acceptable while working on your 
own projects, but eventually people realized that the emphasis on flexibility 
made it difficult to maintain large projects over long periods of time. It was 
difficult, tedious, and time-consuming to review code and try to figure out 
what someone else was thinking when they were solving a complex problem.
Experienced Python programmers will encourage you to avoid complexity and aim for simplicity whenever possible. The Python community’s 
philosophy is contained in “The Zen of Python” by Tim Peters. You can 
access this brief set of principles for writing good Python code by entering import this into your interpreter. I won’t reproduce the entire “Zen of 
Variables and Simple Data Types 35
Python” here, but I’ll share a few lines to help you understand why they 
should be important to you as a beginning Python programmer.
The Zen of Python by Tim Waters:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!



Summary
In this chapter you learned to work with variables. You learned to use 
descriptive variable names and how to resolve name errors and syntax errors when they arise. You learned what strings are and how to 
display strings using lowercase, uppercase, and titlecase. You started 
using whitespace to organize output neatly, and you learned to strip 
unneeded whitespace from different parts of a string. You started working 
with integers and floats, and you read about some unexpected behavior 
to watch out for when working with numerical data. You also learned to 
write explanatory comments to make your code easier for you and others 
to read. Finally, you read about the philosophy of keeping your code as 
simple as possible, whenever possible.
In Chapter 3 you’ll learn to store collections of information in variables 
called lists. You’ll learn to work through a list, manipulating any information in that list.