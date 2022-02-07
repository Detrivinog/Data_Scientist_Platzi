const Car = require("./Car")
const Account = require("./Account")

var car = new Car("Aw456", new Account("Andres Herrera", "abc123"))
car.passenger = 4
car.printDataCar()