
### Developing heritage

class vehicles :

    def __init__(self,color,license_plate,n_wheels) -> None:
        self.color = color
        self.license_plate = license_plate
        self.n_wheels = n_wheels

    def start_engine(self) -> str:
        print("starting engine...")
        print("engine running!")
    
class car(vehicles):
    pass


### Demonstrating how inheritance works

car = car("red","abcd-123",4)
print(car)
car.start_engine()