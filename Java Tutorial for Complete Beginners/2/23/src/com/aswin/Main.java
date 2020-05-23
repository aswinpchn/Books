package com.aswin;

class Person {
  private String name;
  private int age;
  public static String className; // static variables will be generally public.
  public static int objectCount = 0; // To have a count of number of objects created.
  public final static double CONSTANT_VALUE = 3.14; // This is to showcase a usecase of static, (storing constant variables.)

  Person() {
    System.out.println("Person constructor");
    objectCount++;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }

  // You can access both instance variables and static variables inside a normal method.
  public void someMethod() {
    System.out.println(className);
    System.out.println(age);
  }

  public static void someStaticMethod() {
    System.out.println(className);
    //System.out.println(age); // You cant access instance variable inside a static function.
  }

  @Override
  public String toString() {
    return "Person{" +
      "name='" + name + '\'' +
      ", age=" + age +
      '}';
  }
}

public class Main {

  // This repo can exist as a one stop shop about static variables and methos. So informative.

  public static void main(String[] args) {
    // Even before any object for the class is instantiated, we can access static varibles. This shows that only once static variable exist for a class and not for any its instances.
    Person.className = "Person";
    System.out.println(Person.className);

    Person.someStaticMethod();// See, even before any object creation, you can access static method using class Name.

    System.out.println("Person Object count is:" + Person.objectCount);
    Person person = new Person();
    System.out.println("Person Object count is:" + Person.objectCount);

    person.setName("Aswin");
    person.setAge(23);

    System.out.println(person.toString());
    System.out.println(Person.CONSTANT_VALUE);
  }

  /*
    What are the use cases of static variables.
    1. To have a variable, that exists only once for a class and not for each instances.
    2. For Exporting constant variables in some java classes like Math.PI

    Note:
    1. You can access both instance variables and static variables inside a normal method.
    2. You cant access instance variable inside a static function. Coz static method can exist even before any object creation.
   */
}
