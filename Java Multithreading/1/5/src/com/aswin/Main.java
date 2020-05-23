package com.aswin;

import java.util.Scanner;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

class Process extends Thread {

  int id;

  public Process(int id) {
    this.id = id;
  }

  public void run() {

    System.out.println("Staring: " + id + " with " + Thread.currentThread().getId());

    try {
      Thread.sleep(500);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }

    System.out.println("Completed: " + id);
  }
}

public class Main {

  public static void main(String[] args) {

    ExecutorService executor = Executors.newFixedThreadPool(2); // This will create a Thread pool of size 2.

    for(int i = 0; i < 5; i++) {
      executor.submit(new Process(i)); // Here we submit the threads to the executor.
    }

    executor.shutdown(); // Initiates an orderly shutdown in which previously submitted tasks are executed, but no new tasks will be accepted.

    try {
      executor.awaitTermination(10, TimeUnit.SECONDS); // After using the shutdown() method, you can call awaitTermination() to block until all of the started tasks have completed.
    } catch (InterruptedException e) {
      e.printStackTrace();
    }

    System.out.println("End of program."); // Will wait till awaitTermination time periods.
  }

  /*

    Thread pool is an important concept in concurrent programming. as thread creation and deletion is an overhead. having a ready pool gives good performance.

    ExecutorService class is used to create Thread pool in Java.

    All other methods are commented.

    https://www.udemy.com/course/java-multithreading/learn/lecture/108992#overview
    https://www.geeksforgeeks.org/thread-pools-java/
    https://stackoverflow.com/questions/1562079/how-to-stop-the-execution-of-executor-threadpool-in-java

    NOTE:
      There are some risks with pool like Deadlock possibility and context switching overhead. (See GFG for more details.s)
   */
}
