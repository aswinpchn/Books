package com.aswin;

// https://www.geeksforgeeks.org/enum-customized-value-java/
public enum Fruit {
  APPLE("RED"), BANANA("YELLOW"), GRAPES("GREEN"); // As said, Enums are internally class, to give parameters to them, you have to manually write constructors.

  // This is to store the internal parameter within each enum.
  String color;

  // Getter is needed.
  public String getColor() {
    return color;
  }

  private Fruit(String color) {
    this.color = color;
  }
}
