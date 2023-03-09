# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

def zero(operation=None):
    if operation:
        return operation(0)
    else:
        return 0

def one(operation=None):
    if operation:
        return operation(1)
    else:
        return 1

def two(operation=None):
    if operation:
        return operation(2)
    else:
        return 2

def three(operation=None):
    if operation:
        return operation(3)
    else:
        return 3

def four(operation=None):
    if operation:
        return operation(4)
    else:
        return 4

def five(operation=None):
    if operation:
        return operation(5)
    else:
        return 5

def six(operation=None):
    if operation:
        return operation(6)
    else:
        return 6

def seven(operation=None):
    if operation:
        return operation(7)
    else:
        return 7

def eight(operation=None):
    if operation:
        return operation(8)
    else:
        return 8

def nine(operation=None):
    if operation:
        return operation(9)
    else:
        return 9

def plus(x):
    return lambda y: y + x

def minus(x):
    return lambda y: y - x

def times(x):
    return lambda y: y * x

def divided_by(x):
    return lambda y: y // x if x != 0 else "Error: Division by zero"

  
# Test
test.describe('Basic Tests')
test.assert_equals(seven(times(five())), 35)
test.assert_equals(four(plus(nine())), 13)
test.assert_equals(eight(minus(three())), 5)
test.assert_equals(six(divided_by(two())), 3)
