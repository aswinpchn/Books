package com.aswin;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Machine m1 = new Camera();
    m1.work();

    Machine m2 = new Car();
    m2.work();
  }

  /*

    Both abstract class and interface is used for abstraction feature in Java.

    The difference is that interface will only only have abstract methods. But abstract class can have both abstract methods and normal attributes also and that can be extended and used.

    https://www.geeksforgeeks.org/difference-between-abstract-class-and-interface-in-java/
   */

}
