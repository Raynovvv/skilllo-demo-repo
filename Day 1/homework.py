import math


def first():
    print('Hello , World!')


def second():
    name = 'Chris'
    age = 28
    fav_color = 'purple'
    print(f'My name is {name} , I am {age} years old and my color is {fav_color}')


def third():
    a = int(input('Enter length:\n'))
    b = int(input('Enter width:\n'))
    print(a * b)


def fourth():
    temp_f = int(input('Temperature in Fahrenheit:\n'))
    print('Temp in celsius is :', round((temp_f - 32) * (5 / 9)))


def fifth():
    a = int(input('Enter first value:\n'))
    b = int(input('Enter second value:\n'))

    print('Sum is:', (a + b), 'Difference is:', (a - b), 'Product is:', (a * b), 'Quotient is:', (a // b), sep='\n')


def sixth():
    a = int(input('Enter radius:\n'))
    print('Area is:', round(((a ** 2) * math.pi), 2), 'Circumference is: ', round(2 * math.pi * a, 2))


def seventh():
    a = int(input('Enter number:\n'))
    if a % 2 == 0:
        print(a, 'is even number')
    else:
        print(a, 'is odd number')


def eight():
    age = int(input('Enter your age:\n'))
    if age < 18:
        print('You have no right to vote')
    else:
        print('Go vote')


def ninth():
    string = input('Enter a string:\n')

    print(len(string))


def tenth():
    string1 = input('Enter a string:\n')
    string2 = input('Enter another string:\n')

    print(string1 + string2)

# first()
# second()
# third()
# fourth()
# fifth()
# sixth()
# seventh()
# eight()
# ninth()
# tenth()
