package com.aswin;

public class Main {

  public static void main(String[] args) {

    Vehicle vehicle = new Vehicle();
    vehicle.start();
    vehicle.stop();

    Car car = new Car();
    car.start();
    car.stop();

    /*
      Output:

      Vehicle is starting!
      Vehicle is stopping
      Car is starting!
      Vehicle is stopping

      If you see,
        car start is giving this because we are overriding start method in car that is inherited from vehicle.
        car stop is giving this because we are not overriding stop method in car that is inherited from vehicle.
     */
  }

}
