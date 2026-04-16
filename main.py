class Car:
    def __init__(self, model, speed=0):
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10

c = Car("BMW")
c.accelerate()
print(c.speed)
