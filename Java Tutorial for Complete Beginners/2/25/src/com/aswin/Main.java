package com.aswin;

class Person {
  int age;
  String name;

  Person() {
    age = 23;
    name = "aswin";
  }
}

public class Main {

  public static void main(String[] args) {

    // Object class is one important thing in Java, all class implicity extend Object class.
    // https://stackoverflow.com/questions/31019157/how-do-all-classes-inherit-from-object
    Object obj = new Object();
    System.out.println(obj.toString());

    Person person = new Person();
    System.out.println(person.toString()); // We didn't define toString in person object, but it still has toString() method.

    // Object class has toString(), hashCode() and equals() method.
  }

}
