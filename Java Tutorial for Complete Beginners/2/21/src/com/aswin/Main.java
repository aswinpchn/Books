package com.aswin;

class Person {
  private String name;
  private int age;

  public String getName() {
    return name;
  }

  // this.name referes to the object's name and the one without this is the parameter. (Used in setName as there is ambiguit in setName scope).
  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
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

  public static void main(String[] args) {

    System.out.println("Hello World!");

    Person person = new Person();

//    You can't access the variables of other class directly when its private, there needs to getter, setter for that.
//    person.name = "Aswin";
//    person.age = 23;

    // Using getter setter is called Encapsulation (https://stackoverflow.com/questions/742341/difference-between-abstraction-and-encapsulation)
    person.setName("Aswin");
    person.setAge(23);

    System.out.println(person.toString());
  }
}
