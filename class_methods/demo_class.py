class Demo:
    class_var = 'shared variable'

    def __init__(self, value):
        self.instance_var = value

d1 = Demo(100)
d2 = Demo(200)

d1.another_var = 'another variable in the object'

print('contents of d1:', d1.__dict__)
print('contents of d2:', d2.__dict__)

print(Demo.class_var)
print(Demo.__dict__)

# Uses for class variable
'''
As a class variable is present before any instance of the class is created, it can be used to store some meta data relevant to the class, rather than to the instances:

fixed information like description, configuration, or identification values;
mutable information like the number of instances created (if we add a code to increment the value of a designated variable every time we create a class instance)

'''