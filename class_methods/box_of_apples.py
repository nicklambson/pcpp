import random

class Box():
    apples_processed = 0
    total_weight = 0

    def __init__(self):
        pass

    def add_apple(self, apple_weight):
        Box.apples_processed += 1
        Box.total_weight += apple_weight

my_box = Box()

while True:
    apple_weight = random.uniform(0.2, 0.5)
    if Box.total_weight + apple_weight < 300:
        my_box.add_apple(apple_weight)
    else:
        print(my_box.apples_processed)
        print(my_box.total_weight)
        break