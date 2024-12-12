# import first,second

# first.add()
# second.sub()

# Abstraction

from abc import ABC,abstractmethod
class Car(ABC):
    def show(self):
        print("Evry car has 4 wheels")
    @abstractmethod
    def Speed(self):
        pass

class Suzuki(Car):
    def Speed(self):
        print("speed is 100km/h")

class Maruti(Car):
    def Speed(self):
        print("speed is 80km/h")

obj1=Suzuki()
obj1.show()
obj1.Speed()

obj2=Maruti()
obj2.show()
obj2.Speed()
        
