package com.aswin;

// Any class that implements Runnable interface must implement the code for run().
class Runner implements Runnable {

  // This will be called when start is called for threads that use this Thread1.
  public void run() {
    for(int i = 0; i < 10; i++) {
      System.out.println("Hello:" + i);

      try {
        System.out.println(Thread.currentThread().getId());
        Thread.sleep(100);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }
}

public class Main {

  public static void main(String[] args) {

    Thread t1 = new Thread(new Runner()); // We can also use anonymous class to avoid writing implementation for Thread1 class.
    t1.start(); // The run method of the Thread1 class will be called when we call start.

    Thread t2 = new Thread(new Runner());
    t2.start();

    Thread t3 = new Thread(new Runnable() {

      public void run() {
        System.out.println("Thread created using Anonymous class is running");
      }
    });
    t3.start();


  }

  /*

    Multithreading is a Java feature that allows concurrent execution of two or more parts of a program for maximum utilization of CPU. Each part of such program is called a thread. So, threads are light-weight processes within a process.

    Once the start method is called, the contents inside run() will execute and simultaneously the next lines of code in main program will also run...

    Threads can be created by using two mechanisms :
    1. Extending the Thread class
    2. Implementing the Runnable Interface

    https://www.geeksforgeeks.org/multithreading-in-java/
    https://www.udemy.com/course/java-multithreading/learn/lecture/107238#overview

   */
}
