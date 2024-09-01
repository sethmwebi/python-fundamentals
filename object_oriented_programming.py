class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def display_info(self) -> None:
        print(f"Make: {self.make} \nModel: {self.model} \nYear: {self.year}")


car = Car("Mercedes Benz", "E250", 2016)
car.display_info()
