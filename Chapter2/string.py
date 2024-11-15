#practice using strings - #Melvin Khakabo 15.11.2024 - Chapter 2

name = "ada lovelace"
print (name)

#change the case of the words in a string
print(name.title()) #makes the first letter of each word capital
print(name.upper()) #makes each word capital
print(name.lower()) #makes each word lowercase

#Combining or Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
#print(f"Hello, {full_name.title()}!")
message = "Hello, " + full_name.title() + "!"
print(message)

#adding tabs to strings
print("Python") #no tab
print("\tPython") #tab

#adding newlines to strings
print("Languages:\nPython\nC\nJavaScript") 

#combine tabs and newlines in a single string
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#removing whitespace
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip()) #removes whitespace from the right
print(favorite_language.lstrip()) #removes whitespace from the left
print(favorite_language.strip()) #removes whitespace from both sides
