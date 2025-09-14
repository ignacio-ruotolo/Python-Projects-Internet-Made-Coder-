# Create a system to track cars in a garage.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"{self.brand} {self.model} started.")

    def stop(self):
        self.is_running = False
        print(f"{self.brand} {self.model} stopped.")


class Garage:
    def __init__(self):
        self.cars = []  # list of Car objects

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.model} was added to the garage.")

    def list_cars(self):
        if not self.cars:
            print("The garage is empty.")
        else:
            print("Cars in the garage:")
            for car in self.cars:
                status = "running" if car.is_running else "stopped"
                print(f"- {car.brand} {car.model} ({status})")


car1 = Car("Toyota", "Corolla")
car2 = Car("Ford", "Mustang")

garage = Garage()

garage.add_car(car1)
garage.add_car(car2)

car1.start()
car2.stop()

garage.list_cars()
