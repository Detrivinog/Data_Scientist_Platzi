class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Account driver1 = new Account("Andres Herrera", "abcd123");
        Car car = new Car("AMQ123", driver1);
        car.passanger = 4;
        System.out.println("Car Licence: " + car.license);
        car.printDataCar();
    }
}