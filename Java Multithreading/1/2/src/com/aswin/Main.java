package com.aswin;

import java.util.Scanner;

class Thread1 extends Thread {

  volatile boolean running = true; // We have to use volatile here.

  public void run() {

    while(running) {
      System.out.println("Hello.");

      try {
        Thread.sleep(100);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }

  void shutDown() {
    running = false;
  }
}

public class Main {

  public static void main(String[] args) {

    Thread1 t = new Thread1();
    t.start();

    System.out.println("Please return to stop...");
    Scanner scanner = new Scanner(System.in);
    scanner.nextLine();

    t.shutDown();
    System.out.println("Stopped...");
  }

  /*

  What happens when you start a thread is that, there will be a thread that will start in run method. And at the same time, main method contents also will run paralelly by main thread.

  Whenever a thread is ever running, you can stop it by two methods. (https://www.geeksforgeeks.org/killing-threads-in-java/)
    1. Using a variable.
    2. Interrupt method.

  Note: You have to use volatile type of variable for that shutdown flag.
    This is because sometimes the thread may cache the running variable by itself, Then if we change the running variable from outside using the shutdown method. The thread can't get the updated value of "running" variable.
    If you use volatile keyword, the runnign variable wont be cached by the thread and it the thread knows that the "running" variable would change.

   */
}
