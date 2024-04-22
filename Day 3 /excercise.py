# Problem 0:
# Write a program that takes an integer input from the user
# and checks if it's odd or even. Use an if-else statement to print the result.
import random


def problem_0():
    input_number = input("Give me a number:\n")
    if (int(input_number) % 2) == 0:
        print(f"{input_number} is even")
    else:
        print(f"{input_number} is odd")


# problem_0()


# Write a Python program to find the sum of all even numbers from
# 1 to 100 using a loop. Make use of control flow constructs like
# the for loop and conditional statements.
def problem_1():
    i = 1
    sum = 0
    while i <= 100:
        sum += i
        i += 1
    print(sum)


# problem_1()

# Problem 2:
# Write a Python script that prompts the user in the console a simple problem
# ( how much does 5 + 17 equal to ) until the user provides a correct answer.

def problem_2():
    num_1 = random.randrange(1, 100)
    num_2 = random.randrange(1, 100)
    print(f"Whats the result of {num_1} + {num_2} ?\n")
    sum_of_nums = int(num_1) + int(num_2)
    user_input = int(input())
    while user_input != sum_of_nums:
        print(f"{user_input} is not correct answer. Try again : \n")
        user_input = input()
    print(f"{user_input} is correct!")


# problem_2()

# Problem 3:
# Write a Python script that iterates over the first 1000 numbers and prints "Fizz" if the number is divisible by 3,
# "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both 3 and 5.

def problem_3():
    numbers = range(1, 1000)
    for num in numbers:
        if int(num) % 3 and int(num) % 5:
            print("FizzBuzz")
        elif num % 5:
            print("Buzz")
        elif num % 3:
            print("Fizz")


# problem_3()

# Problem 4:
# Design a Python program that simulates a simple guessing game.
# The program should generate a random number between 1 and 100 and ask the user to guess it.
# Provide hints like "Too high" or "Too low" until the user guesses the correct number. Use a while loop for this game.

def problem_4():
    random_num = random.randrange(1, 100)
    user_input = int(input("Enter a number:\n"))
    while True:
        if user_input < random_num:
            print("Too low")
            user_input = int(input("Try again:\n"))
        elif user_input > random_num:
            print("Too high")
            user_input = int(input("Try again:\n"))
        else:
            print("Got it!")
            break


# Problem 5:
# Modify problem 2 so that every time the user is prompted the problem is different.
# Think of a way to design that and come up with a proper solution for that.

def problem_5():
    num_1 = random.randrange(1, 100)
    num_2 = random.randrange(1, 100)
    print(f"Whats the result of {num_1} + {num_2} ?\n")
    sum_of_nums = int(num_1) + int(num_2)
    user_input = int(input())
    while user_input != sum_of_nums:
        print(f"{user_input} is not correct answer. Try again : \n")
        num_1 = random.randrange(1, 100)
        num_2 = random.randrange(1, 100)
        print(f"Whats the result of {num_1} + {num_2} ?\n")
        sum_of_nums = int(num_1) + int(num_2)
        user_input = int(input())
    print(f"{user_input} is correct!")


# problem_5()

# Problem 6:
# Write a Python program that takes an integer input from the user and
# prints the multiplication table for that number from 1 to 10 using a for loop.

def problem_6():
    user_input = int(input("Give me a number:\n"))
    range_of_nums = range(1, 11)
    for x in range_of_nums:
        print(user_input * int(x))


# problem_6()

# Problem 7:
# Create a Python program that checks if a given integer is a prime number.
# Use a for loop to iterate through possible divisors and use an if-else statement to determine if it's prime.

def problem_7():
    num = int(input("Give me an number:\n"))
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")


# problem_7()

# Problem 8: Pattern Printing
# Write a program that takes an integer 'n' as input and prints the following pattern using nested for loops:

def problem_8():
    input_num = int(input("Give me a num:\n"))
    for i in range(1, input_num + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

problem_8()