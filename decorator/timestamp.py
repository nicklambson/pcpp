from datetime import datetime

def print_time(function):
    print(datetime.now())
    return function

@print_time
def add_two_integers(x, y):
    print(f"{x} + {y} = {x+y}")

@print_time
def multiply_two_integers(x, y):
    print(f"{x} x {y} = {x*y}")

@print_time
def subtract_two_integers(x, y):
    print(f"{x} - {y} = {x-y}")

add_two_integers(15, 29)

multiply_two_integers(15, 29)
subtract_two_integers(15, 29)

