package com.aswin;

// Bike is implementing Vehicle, so two methods must be implemented.
public class Bike implements Vehicle {

  int speed;

  public Bike() {
    this.speed = 0;
  }

  @Override
  public void speedUp() {
    speed += 1;
  }

  @Override
  public void slowDown() {
    speed -= 1;
  }
}
