class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

# dot notation
drake.quack()
print(duckling.height)

# class 'type'
print(Duck.__class__)
# class '__main__.Duck'
print(duckling.__class__)
# class 'str'
print(duckling.sex.__class__)
# class 'method'
print(duckling.quack.__class__)
