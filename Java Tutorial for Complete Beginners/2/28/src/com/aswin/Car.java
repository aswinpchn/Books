package com.aswin;

// Car is implementing Vehicle, so two methods must be implemented.
public class Car implements Vehicle {

  int speed;

  public Car() {
    this.speed = 0;
  }

  @Override
  public void speedUp() {
    speed += 2;
  }

  @Override
  public void slowDown() {
    speed -= 2;
  }
}
