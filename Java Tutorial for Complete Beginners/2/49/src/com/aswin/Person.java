package com.aswin;

import java.io.Serializable;

// Without serializable, it will give java.io.NotSerializableException: com.aswin.Person
public class Person implements Serializable {

  String name;
  int age;

  public Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  @Override
  public String toString() {
    return "Person{" +
      "name=" + name +
      ", age=" + age +
      '}';
  }
}
