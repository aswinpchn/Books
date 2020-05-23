package com.aswin;

import java.util.Scanner;

class Thread1 extends Thread {

  public void run() {

    System.out.println(Thread.currentThread().getName()); // Thread.currentThread().getName() is a static method that gets name of currently executing thread.

    while(!Thread.currentThread().isInterrupted()) {
      System.out.println("Hello." + Thread.currentThread().getName() + " " + Thread.currentThread().isInterrupted());

      for(int i = 0; i < 1E8; i++) {

      }
    }

    System.out.println(Thread.currentThread().getName() + " " + Thread.currentThread().isInterrupted());
  }
}

public class Main {

  public static void main(String[] args) {

    System.out.println(Thread.currentThread().getName());

    Thread1 t = new Thread1();
    t.start();

    System.out.println("Please return to stop...");
    Scanner scanner = new Scanner(System.in);
    scanner.nextLine();

    t.interrupt(); // t.interrupt() is an instance method. It will call the interrupt functionality on t Thread object.
    System.out.println("Stopped...");
  }

  /*

    What happens when you start a thread is that, there will be a thread that will start in run method. And at the same time, main method contents also will run paralelly by main thread.

    Whenever a thread is ever running, you can stop it by two methods. (https://www.geeksforgeeks.org/killing-threads-in-java/)
      1. Using a variable.
      2. Interrupt method. (This program)(https://www.udemy.com/course/java-multithreading/learn/lecture/139737#overview)

    Note: (https://stackoverflow.com/questions/1904072/java-difference-in-usage-between-thread-interrupted-and-thread-isinterrupted)
    t.interrupt(); -->  t.interrupt() is an instance method. It will call the interrupt functionality on t Thread object.
    Thread.currentThread().interrupt(); --> This is a static method, it called on current thread that is executing.

   */
}
