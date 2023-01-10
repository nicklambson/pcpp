# wrong: should ask the user for an int
number = input("Enter a number: ")
multiply_number_by_two = number * 2

print("Your number multiplied by two is:", multiply_number_by_two)

# better because Python will shout the error
number = int(input("Enter a number: "))
multiply_number_by_two = number * 2

print("Your number multiplied by two is:", multiply_number_by_two)

# wrong: the exception is too broadly handled.
try:
    print(1/0)
except Exception as e:
    pass

# better: handles a specific kind of error

try:
    print(1/0)
except ZeroDivisionError:
    print("Don't divide by zero!")