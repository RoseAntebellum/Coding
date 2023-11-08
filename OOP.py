class Car:

    def __init__(self, color, miles):
        self.color = color
        self.miles = miles
    
    def __str__(self):
        return f"The {self.color} car has {self.miles} Miles"
    
blue = Car("blue", 20000)
print(blue)
red = Car("red", 30000)
print(red)