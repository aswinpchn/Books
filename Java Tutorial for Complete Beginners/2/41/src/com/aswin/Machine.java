package com.aswin;

// We are defining an abstract class, This class can't be directly instantiated.
public abstract class Machine {
  private String name;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public abstract void work();
}
