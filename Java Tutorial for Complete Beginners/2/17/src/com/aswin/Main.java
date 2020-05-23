package com.aswin;

// You can have any number of non-public classes in a .java file.
class Person {
  String name;
  int age;

  @Override
  public String toString() {
    return "Person{" +
      "name='" + name + '\'' +
      ", age=" + age +
      '}';
  }
}

// In any .java file, you can onyl have one public class. There can be many non-public classes though.
public class Main {

  public static void main(String[] args) {

    System.out.println("Hello World!");

    Person person = new Person();
    person.name = "Aswin";
    person.age = 23;

    System.out.println(person.toString());
  }
}
