class Duration():
    def __init__(self, hours=0, minutes=0, seconds=0):
        if not all(isinstance(x, int) for x in (hours, minutes, seconds)):
            raise Exception("All arguments must be integers")
        else:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            
    def total_seconds(self):
        return self.seconds + self.minutes * 60 + self.hours * 3600

    def __str__(self):
        padded_hours = ("0" + str(self.hours))[-2:]
        padded_minutes = ("0" + str(self.minutes))[-2:]
        padded_seconds = ("0" + str(self.seconds))[-2:]
        return str(padded_hours) + ":" + str(padded_minutes) + ":" + str(padded_seconds)

    def __add__(self, other):
        if not isinstance(other, int):
            raise Exception("Must add an integer")
        else:
            result = self.total_seconds() + other
            self.hours, remainder = divmod(result, 3600)
            self.minutes, remainder = divmod(remainder, 60)
            self.seconds = remainder
            return self

    def __sub__(self, other):
        if not isinstance(other, int):
            raise Exception("Must add an integer")
        else:
            result = self.total_seconds() - other
            self.hours, remainder = divmod(result, 3600)
            self.minutes, remainder = divmod(remainder, 60)
            self.seconds = remainder
            return self




my_duration = Duration(hours=123)

# my_duration -= 567
print(my_duration)