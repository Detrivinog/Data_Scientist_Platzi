from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola mundo")


    car = Car("AMS234", Account("Andres Herrera", "Anda876"))
    print(vars(car))
    print(vars(car.driver))