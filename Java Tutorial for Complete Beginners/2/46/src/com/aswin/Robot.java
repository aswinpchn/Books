package com.aswin;

public class Robot {
  private int id;

  public Robot(int id) {
    this.id = id;
  }

  private class Brain {
    public void think() {
      System.out.println("Robot: " + id + " is thinking"); // You can access outer class variable from inside.
    }
  }

  public void start() {
    System.out.println("Starting robot: " + id);

    Brain b = new Brain();
    b.think();
  }
}
