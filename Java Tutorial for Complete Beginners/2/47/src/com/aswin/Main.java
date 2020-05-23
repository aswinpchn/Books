package com.aswin;

import java.util.Arrays;

public class Main {

  public static void main(String[] args) {

    Animal animal = Animal.DOG; // animal variable of type Animal holds Animal.DOG

    // This is a new feature in java switch. If you give enum as the parameter, the case can directly be the contents of enum.
    switch (animal) {
      case CAT:
        System.out.println("Cat");
        break;
      case DOG:
        System.out.println("Dog");
        break;
      case MOUSE:
        System.out.println("Mouse");
        break;
    }

    System.out.println(animal);
    System.out.println(Animal.DOG);


    System.out.println(Fruit.APPLE); // APPLE,
    System.out.println(Fruit.APPLE.name()); // APPLE,
    System.out.println(Fruit.APPLE.getColor()); // RED


    System.out.println(Arrays.toString(Fruit.values())); // Array of all enums
  }

  /*
    Enumerations serve the purpose of representing a group of named constants in a programming language.
    Enums are internally represented using classes only.

    https://www.geeksforgeeks.org/enum-in-java/
    https://www.geeksforgeeks.org/enum-customized-value-java/
    https://www.udemy.com/course/java-tutorial/learn/lecture/313423#overview

   */
}
