#Hands-on practice - #Melvin Khakabo 15.11.2024 - Chapter 2

#Write a separate program to accomplish each of these exercises. 
# Save each program with a filename that follows standard Python conventions, using lowercase letters and underscores, 
# such as simple_message.py and simple_messages.py.
#2-1. Simple Message: Store a message in a variable, and then print that message.
#2-2. Simple Messages: Store a message in a variable, and print that message.
#Then change the value of your variable to a new message, and print the new message

#answer 2.1
message = "Hello Python Crash Course reader!"
print(message)

#answer 2.2
message = "Hello Python Crash Course reader!"
print(message)

message = "Hello Python Crash Course readers!" #an S is added to reader and prints out the new message with changes
print(message)



#2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. 
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
#2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, 
# uppercase, and titlecase.
#-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
# Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called 
# famous_person. Then compose your message and store it in a new variable called message. Print your message.
#2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each 
#character combination, "\t" and "\n", at least once.Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip()

#answer 2.3
name = "ada lovelace"
print(f"Hello {name.title()}, would you like to learn some Python today?")

#answer 2.4
name = "ada lovelace"
print(f"Hello {name.title()}") #prints the name in lowercase
print(f"Hello {name.upper()}") #prints the name in uppercase
print(f"Hello {name.title()}") #prints the name in titlecase

#answer 2.5
quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"
print(f"{author} once said, \"{quote}\"")

#answer 2.6
quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"
print(f"{author} once said, \"\n{quote}")

#answer 2.7
name = "\tada lovelace\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())


#2-8. Number Eight: Write addition, subtraction, multiplication, and division 
#operations that each result in the number 8. Be sure to enclose your operations 
#in print statements to see the results. You should create four lines that look 
#like this:print(5 + 3)
#Your output should simply be four lines with the number 8 appearing once on each line.
#2-9. Favorite Number: Store your favorite number in a variable. Then, using 
#that variable, create a message that reveals your favorite number. Print that message.

#answer 2.8
print(2 + 6)
print(10 - 2)
print(2 * 4)
print(16 / 2)

#answer 2.9
favorite_number = 8
print(f"My favorite number is {favorite_number}.")


#2-10. Adding Comments: Choose two of the programs you’ve written, and 
#add at least one comment to each. If you don’t have anything specific to write 
#ecause your programs are too simple at this point, just add your name and 
#the current date at the top of each program file. Then write one sentence 
#describing what the program does


#2-11. Zen of Python: Enter import this into a Python terminal session and skim 
#through the additional principles.