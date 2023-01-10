class Wax:
    def melt(self):
        print("Wax can be used to form a tool")

class Cheese:
    def melt(self):
        print("Cheese can be eaten")

class Wood:
    def fire(self):
        print("A fire has been started!")

for element in Wax(), Cheese(), Wood():
    try:
        element.melt()
    except AttributeError:
        print('No melt() method')

'''polymorphism is used when different class objects share conceptually similar methods (but are not always inherited), like melt().
polymorphism leverages clarity and expressiveness of the application design and development;
when polymorphism is assumed, it is wise to handle exceptions that could pop up.
'''