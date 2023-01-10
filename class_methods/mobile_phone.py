class MobilePhone:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return print(f"mobile phone {self.number} is turned on.")

    def turn_off(self):
        return print(f"mobile phone {self.number} is turned off.")

    def calling(self, call_number):
        return print(f"{self.number} is calling {call_number}")

phone_1 = MobilePhone("01632-960004")
phone_2 = MobilePhone("01632-960012")

phone_1.turn_on()
phone_2.turn_on()
phone_1.calling(phone_2.number)
phone_1.turn_off()
phone_2.turn_off()

