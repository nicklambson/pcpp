class MobilePhone:
    def __init__(self, number):
        self.number = number
    
    def turn_on(self):
        print(f"mobile phone {self.number} is turned on.")
        return f"mobile phone {self.number} is turned on."
        
    def turn_off(self):
        print(f"mobile phone {self.number} is turned off.")
        return f"mobile phone {self.number} is turned off."
        
    def call(self, number):
        print(f"calling {number}")
        return f"calling {number}"
        
m1 = MobilePhone("01632-960040")
m2 = MobilePhone("01632-960012")

m1.turn_on()
m2.turn_on()
m1.call("555-34343")
m1.turn_off()
m2.turn_off()