'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''
name= input("What is your name? ")
age= input("What is your age? ")
year= 2022 - int(age) + 100
message = name + ' will be 100 years old in ' + str(year) 
print(message)
number= input("Enter a number: ")

