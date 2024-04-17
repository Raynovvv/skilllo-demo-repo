# Exercise 1: Online Shopping Discount

# Given a variable `total_amount` representing the total amount in the shopping cart,
# write a program that prints a discount message if the total amount is over $100,
# and always prints a 'thank you' message.

total_amount = 120  # Fill in the total amount here


def first(total_amount):
    if total_amount >= 120:
        print('You have discount')
    print('Thank you!')


# Exercise 2: Temperature Checker

# Given a variable `temperature` representing the current temperature in Celsius,
# write a program that prints "Warm" if the temperature is greater than or equal to 25 degrees Celsius,
# otherwise print "Cool".

temperature = 22  # Fill in the temperature here


def second(temp):
    if temp >= 25:
        print('Warm\n')
    else:
        print('Cool\n')


...

# Exercise 3: Time of the Day

# Given a variable `hour` representing the current hour (in 24-hour format),
# write a program that prints "Good Morning" if the hour is before 12 (12 inclusive),
# "Good Afternoon" if the hour is between 12 and 17 (17 inclusive),
# and "Good Evening" if the hour is after 17.

hour = 15  # Fill in the hour here


def third(hour):
    if 5 < hour < 12:
        print('Good Morning!')
    elif 12 < hour < 17:
        print()


...


# Exercise 4: Secret Message

# Given a variable `message` representing a secret message,
# write a program that prints "Message found" if the message is not empty,
# otherwise print "No message".

def fourth():
    message = ""  # Fill in the message here
    if message:
        print("Message found")
    else:
        print("No message")


...


# Exercise 5: List Iteration

# You have a list of fruits. Write a program that iterates over each fruit in the list and prints each fruit's name.
def fifth():
    fruits = ["Apple", "Banana", "Orange", "Grape", "Watermelon"]
    for x in fruits:
        print(x)


...


# Exercise 6: Range Iteration

# Write a program that prints all the even numbers from 1 to 20 using a for loop and the range() function.
def sixth():
    numbers = range(1, 21)
    for x in numbers:
        print(x)


...


# Exercise 7: While Loop

# Write a program using a while loop to find the sum of all numbers from 1 to 100.
def seventh():
    i = 1
    sum = 0
    while i <= 100:
        sum += i
        i += 1
    print(sum)


...

# Exercise 8: Number of Friends

# Write a program that asks how many friends you have and then asks for each of their names.

num_friends = 2


def eight(friends):
    for x in range(friends):
        input("Enter a name for your friend:\n")


# Exercise 9: Guess the Number
# Write a program that has a number and keeps asking the user to input a number until the user guesses it.

secret_number = 42


def ninth(number):
    guess = input("Enter a number:\n")
    while not int(number) == int(guess):
        guess = input("Try again:\n")
    print("You guessed it!")


...


# Exercise 10: Multiplication Table

# Generate the multiplication table for the numbers 1 to 9.

def tenth():
    nums_to_multiply = range(1, 11)
    for x in nums_to_multiply:
        for i in nums_to_multiply:
            print(i * x)


# Exercise 11: continue

# Do the same as in Exercise 6 but do not print the number 10. Use `continue` do achieve this
def eleventh():
    numbers = range(1, 21)
    for x in numbers:
        if int(x) == 10:
            continue
        print(x)


...

# Exercise 12: Password Checker

# Write a program that asks the user to enter a password. If the password is correct, print a message saying
# "Access granted" and end the program. If the user enters the wrong password three times, print "Access denied" and
# end the program..

correct_password = "learnpythonwithskillo"


def twelfth(password):
    i = 0
    while True:
        user_input = input("Enter your password:\n")
        i += 1
        if user_input == password:
            print("Access granted")
            break
        if user_input != password and i >= 3:
            print("Access denied")
            break


...
#first(total_amount)
#second(temperature)
#eight(num_friends)
#ninth(secret_number)
#eleventh()
#twelfth(correct_password)
#tenth()
