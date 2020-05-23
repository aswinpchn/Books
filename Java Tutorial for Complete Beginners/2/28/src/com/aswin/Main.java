package com.aswin;

public class Main {

  public static void main(String[] args) {

    Car car = new Car();
    System.out.println(car.speed);
    car.speedUp();
    System.out.println(car.speed);

    Bike bike = new Bike();
    System.out.println(bike.speed);
    bike.speedUp();
    System.out.println(bike.speed);

    // This is a novel concept. In left side we can keep the type as interface name and in right side, you can give More specific implementation.
    // Common use case is   ->    List<Integer> l = new ArrayList<>();    [When we create list, we think about its storage and all, once created, we can go ahead and forget the implementation specifics.]
    Vehicle car1 = new Car();
    car1.speedUp();
  }

  /*

  Inheritance and Interface:

  Inheritance allows subclass to reuse the features of parent class. (https://www.geeksforgeeks.org/inheritance-in-java/)

  Interfaces specify what a class must do and not how. It is the blueprint of the class. (Abstraction) (https://www.geeksforgeeks.org/interfaces-in-java/)

   */

}
