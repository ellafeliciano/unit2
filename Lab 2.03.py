'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction: i think if you enter to seek the holy grail then it will say go on off you go 
Actual: go on off you go

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: if you type in one of the coloros it will say something. if you type in a different color it will say it doesn't recognize that color.
Actual: if you type in one of the coloros it will say something. if you type in a different color it will say it doesn't recognize that color.

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

# get 3 sides of a triangle from user
x = int(input("What is x?"))
y = int(input("What is y?"))
z= int(input("What is z?"))

# can it be a triangle
if x + y > z and x + z > y and y + z > x:
    print(f"Perimeter of the triangle is: {x + y + z}")

    # is it a right triangle
    if x ** 2 + y ** 2 == z ** 2:
        print("This is a right triangle.")

    # determine if isoceles, scalene, or eqilateral 
    if x == y and y == z: 
        print("This is an eqilateral triangle.")
    elif x == y or z == y or x == z:
        print("This is an isoceles triangle.")
    else:
        print("This is a scalene triangle.")

else:
    print("Sorry, these inputs do not make a triangle")

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
print("Welcome to my game show!")
prize_list = ['car', 'puppy', 'bike', 'money', 'candy', 'flatscreen TV', 'kitten', 'movie tickets', 'vacation', 'cow']
user_pick = input("Pick a number between 1-10: ")
user_pick = int(user_pick)
if user_pick == 1:
    print("Congratulations, you have won a car!")
elif user_pick == 2:
    print("Congratulations you have won a puppy!")
elif user_pick == 3:
    print("Congratulations you have won a bike!")
elif user_pick == 4:
    print("Congratulations you have won money!")
elif user_pick == 5:
    print("Congratulations you have won some candy!")
elif user_pick == 6:
    print("Congratulations you have won a flatscreen TV!")
elif user_pick == 7:
    print("Congratulations you have won a kitten!")
elif user_pick == 8:
    print("Congratulations you have won movie tickets!")
elif user_pick == 9:
    print("Congratulations you have won a vacation!")
elif user_pick == 10:
    print("Congratulations you have won a cow!")

